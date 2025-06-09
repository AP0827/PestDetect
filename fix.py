import os
import xml.etree.ElementTree as ET
from tqdm import tqdm

# Modify base path here
BASE_DIR = "dataset/Detection/VOC2007"

ANNOTATIONS_DIR = os.path.join(BASE_DIR, "Annotations")
JPEG_IMAGES_DIR = os.path.join(BASE_DIR, "JPEGImages")
IMAGESETS_DIR = os.path.join(BASE_DIR, "ImageSets", "Main")
OUTPUT_LABELS_DIR = "labels"

# Load class mappings (replace this with actual 102-class names)
# For now, assume class_map.txt is located at:
# dataset/IP102_v1.1-.../Classification/class_map.txt
CLASS_MAP_FILE = "dataset/Classification/classes.txt"

classes = sorted([line.strip() for line in open(CLASS_MAP_FILE)])
class_to_index = {cls: i for i, cls in enumerate(classes)}

def convert_voc_to_yolo(xml_file, img_w, img_h):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    yolo_labels = []

    for obj in root.findall("object"):
        cls_id_str = obj.find("name").text.strip()
        try:
            cls_id = int(cls_id_str)  # directly convert number from XML
        except ValueError:
            print(f"[WARN] Invalid class id '{cls_id_str}' in {xml_file}")
            continue

        # Optionally, check if cls_id is in valid range:
        if cls_id < 0 or cls_id >= len(classes):
            print(f"[WARN] Class id {cls_id} out of range in {xml_file}")
            continue

        xml_box = obj.find("bndbox")
        xmin = float(xml_box.find("xmin").text)
        ymin = float(xml_box.find("ymin").text)
        xmax = float(xml_box.find("xmax").text)
        ymax = float(xml_box.find("ymax").text)

        x_center = ((xmin + xmax) / 2) / img_w
        y_center = ((ymin + ymax) / 2) / img_h
        width = (xmax - xmin) / img_w
        height = (ymax - ymin) / img_h

        yolo_labels.append(f"{cls_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}")

    return yolo_labels

def process_split(split):
    split_file = os.path.join(IMAGESETS_DIR, f"{split}.txt")
    output_dir = os.path.join(OUTPUT_LABELS_DIR, split)
    os.makedirs(output_dir, exist_ok=True)

    with open(split_file, "r") as f:
        image_ids = [line.strip() for line in f.readlines()]

    print(f"[INFO] Processing {len(image_ids)} images for '{split}' split")

    for img_id in tqdm(image_ids):
        xml_path = os.path.join(ANNOTATIONS_DIR, f"{img_id}.xml")
        if not os.path.exists(xml_path):
            continue

        try:
            tree = ET.parse(xml_path)
            root = tree.getroot()
            img_w = int(root.find("size").find("width").text)
            img_h = int(root.find("size").find("height").text)

            yolo_labels = convert_voc_to_yolo(xml_path, img_w, img_h)

            label_file = os.path.join(output_dir, f"{img_id}.txt")
            with open(label_file, "w") as f:
                f.write("\n".join(yolo_labels))

        except Exception as e:
            print(f"[WARN] Error processing {img_id}: {e}")

if __name__ == "__main__":
    for split in ["trainval", "test"]:
        process_split(split)
