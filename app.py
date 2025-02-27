from flask import Flask, render_template, request, Response
import cv2
import os
from src.detection import detect_license_plates
from src.ocr import extract_text_from_plate
from src.logger import log_detection, read_logs

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initialize webcam
cap = cv2.VideoCapture(0)

def detect_and_extract(frame):
    """Detect plates, extract text, and log results."""
    plates = detect_license_plates(frame)

    for x1, y1, x2, y2, plate_crop in plates:
        plate_text = extract_text_from_plate(plate_crop)
        if plate_text != "Not Detected":
            log_detection(plate_text)

        # Draw bounding box & text
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, plate_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame

def generate_frames(source=0):
    """Process video or webcam frames."""
    cap = cv2.VideoCapture(source)
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        frame = detect_and_extract(frame)
        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html', log_entries=read_logs())

@app.route('/video_feed')
def video_feed():
    """Live webcam stream."""
    return Response(generate_frames(0), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/upload_video', methods=['POST'])
def upload_video():
    """Process uploaded video."""
    if 'video' not in request.files:
        return "No file uploaded", 400

    file = request.files['video']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    return Response(generate_frames(file_path), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
