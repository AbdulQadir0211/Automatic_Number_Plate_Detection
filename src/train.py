from ultralytics import YOLO

from ultralytics import YOLO

# Load YOLOv11 model (or a different version if needed)
model = YOLO("yolov11n.pt")  # Use 'n', 's', 'm', 'l', or 'x' for different sizes

# Train the model on your dataset
model.train(
    data="data.yaml",  # Path to your dataset YAML file
    epochs=50,  # Adjust as needed
    batch=16,
    imgsz=640,
    device="cuda"  # Use "cpu" if you don’t have a GPU
)
