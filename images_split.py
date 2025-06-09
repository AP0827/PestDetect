import os
import shutil

BASE_DIR = "dataset/Detection/VOC2007"
IMAGE_DIR = os.path.join(BASE_DIR, "JPEGImages")

# Output folders
OUTPUT_BASE = "dataset_split"
IMAGE_OUTPUT_DIR = os.path.join(OUTPUT_BASE, "images")

# Split files
TRAINVAL_SPLIT = os.path.join(BASE_DIR, "ImageSets", "Main", "trainval.txt")
TEST_SPLIT = os.path.join(BASE_DIR, "ImageSets", "Main", "test.txt")

# Helper to find image file with any extension
def find_image_file(img_id):
    for ext in [".jpg"]:
        path = os.path.join(IMAGE_DIR, img_id + ext)
        if os.path.exists(path):
            return path
    return None

def copy_images(split_txt, split_name):
    with open(split_txt, "r") as f:
        image_ids = [line.strip() for line in f.readlines()]

    os.makedirs(os.path.join(IMAGE_OUTPUT_DIR, split_name), exist_ok=True)

    print(f"[INFO] Copying {len(image_ids)} images to {split_name}/")

    for img_id in image_ids:
        src_img = find_image_file(img_id)
        if src_img:
            dst_img = os.path.join(IMAGE_OUTPUT_DIR, split_name, os.path.basename(src_img))
            shutil.copy2(src_img, dst_img)
        else:
            print(f"[WARN] Image not found for ID: {img_id}")

if __name__ == "__main__":
    copy_images(TRAINVAL_SPLIT, "trainval")
    copy_images(TEST_SPLIT, "test")
