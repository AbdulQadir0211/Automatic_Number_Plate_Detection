# 🚗 Automatic Number Plate Recognition (ANPR) System

A real-time **Automatic Number Plate Recognition (ANPR) system** using **YOLOv11** for license plate detection and **EasyOCR** for text extraction. The system supports **real-time webcam processing** and **video file uploads** with Flask UI and logging.

---

## 🚀 Features

✅ **YOLOv11 for License Plate Detection**  
✅ **EasyOCR for Text Extraction**  
✅ **Live Webcam & Video Upload Processing**  
✅ **Timestamped Logging of Detected Plates**  
✅ **Flask Web UI for Easy Interaction**  
✅ **Dockerized for Deployment on AWS EC2**  

---

## 📂 Project Structure


📂 Project Structure
php
Copy
Edit
/ANPR_Project/src
│── app.py                # Flask API
│── detection.py          # YOLOv11-based detection
│── ocr.py                # EasyOCR-based text extraction
│── logger.py             # Logs detected plates with timestamps
│── requirements.txt      # Python dependencies
│── Dockerfile            # Docker container setup
│── static/               # Static files (if needed)
│── templates/            # HTML UI
│── runs/                 # YOLOv11 model & results
└── logs/                 # Stored detection logs
📦 Installation


1️⃣ **Clone the Repository**
bash '''
Copy
Edit
git clone https://github.com/your-username/ANPR_Project.git
cd ANPR_Project  '''
2️⃣ **Install Dependencies**
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ **Run the Flask App**
bash
Copy
Edit
python app.py
Open http://127.0.0.1:5000/ in your browser.

🛠 **YOLOv11 Model Training**
Download Dataset and prepare it in YOLO format.
Train YOLOv11 using Ultralytics:
bash
Copy
Edit
yolo task=detect mode=train model=yolov11.yaml data=your_data.yaml epochs=50 
Save Best Model Weights to runs/detect/train/weights/best.pt.
📦 Docker Deployment
1️⃣ Build Docker Image
bash
Copy
Edit
docker build -t anpr-system .
2️⃣ Run the Container
bash
Copy
Edit
docker run -d -p 5000:5000 anpr-system
Now, access http://127.0.0.1:5000/.

🚀 Deploy on AWS EC2
Launch Ubuntu EC2 Instance
Install Docker on EC2:
bash
Copy
Edit
sudo apt update && sudo apt install -y docker.io
Transfer Files to EC2
bash
Copy
Edit
scp -i your-key.pem -r ANPR_Project ubuntu@your-ec2-ip:~/
Run the Docker Container
bash
Copy
Edit
docker run -d -p 80:5000 anpr-system
Access the ANPR System
Open http://your-ec2-ip/ in your browser.
📝 Logging & Storage
Detected plates are logged in detections_log.csv with timestamps.
The last 5 detections are displayed on the UI.
