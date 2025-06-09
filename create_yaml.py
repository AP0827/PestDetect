import os
classes_file = "dataset/Classification/classes.txt"
output_yaml = "data.yaml"

# Set full paths to your dataset folders (absolute paths recommended)
images_dir = os.path.abspath("dataset_split/images")
trainval_path = os.path.join(images_dir, "trainval")
test_path = os.path.join(images_dir, "test")

# Read class names
with open(classes_file, "r") as f:
    class_names = [line.strip() for line in f.readlines() if line.strip()]

yaml_content = f"""train: {trainval_path}
val: {test_path}

nc: {len(class_names)}
names: {class_names}
"""

# Write to data.yaml
with open(output_yaml, "w") as f:
    f.write(yaml_content)

print("[INFO] data.yaml generated successfully!")
print(f"[INFO] Path: {os.path.abspath(output_yaml)}")
