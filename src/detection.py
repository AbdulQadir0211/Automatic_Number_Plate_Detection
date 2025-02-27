import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO("models/best.pt")  # Use '/' instead of '\' for better compatibility

def detect_license_plates(frame):
    """Detect license plates in an image frame using YOLOv11."""
    results = model(frame)  # Run inference
    plates = []

    for result in results:  # Iterate through detected objects
        for box in result.boxes:  # Access bounding boxes
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())  # Get coordinates
            conf = round(box.conf[0].item(), 2)  # Confidence score
            class_id = int(box.cls[0].item())  # Class ID

            # Crop the detected plate from the frame
            plate_crop = frame[y1:y2, x1:x2] if y2 > y1 and x2 > x1 else None

            # Store detection details
            plates.append({
                "x1": x1, "y1": y1, "x2": x2, "y2": y2,
                "confidence": conf, "class_id": class_id,
                "plate_crop": plate_crop
            })

            print(f"Detected: {class_id} at ({x1}, {y1}, {x2}, {y2}) with confidence {conf}")

    return plates
