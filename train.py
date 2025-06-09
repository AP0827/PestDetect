from ultralytics import YOLO

# Path to your data.yaml file (adjust path as needed)
data_yaml = "data.yaml"

# Create YOLO model instance with yolov8x weights (pretrained)
model = YOLO("yolov8n.pt")

# Train the model
model.train(
    data=data_yaml,    # Dataset config
    epochs=15,        # You can increase epochs for better accuracy
    imgsz=640,         # Image size (you can try 640 or 1024)
    batch=4,          # Adjust batch size depending on your GPU VRAM
    device=0,          # Use GPU device 0 (default CUDA GPU)
    workers=4,         # Data loader workers
    save=True,         # Save best weights
    name="yolov8n_IP102_best"  # Custom run name
)