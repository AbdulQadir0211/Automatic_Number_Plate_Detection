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
```
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
```

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/ANPR_Project.git
cd ANPR_Project
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask App
```bash
python app.py
```
Now, open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

---

## 🛠 YOLOv11 Model Training
1. Download the dataset and prepare it in YOLO format.
2. Train YOLOv11 using Ultralytics:
```bash
yolo task=detect mode=train model=yolov11.yaml data=your_data.yaml epochs=50
```
3. Save the best model weights to:
```
runs/detect/train/weights/best.pt
```

---

## 📦 Docker Deployment

### 1️⃣ Build Docker Image
```bash
docker build -t anpr-system .
```

### 2️⃣ Run the Container
```bash
docker run -d -p 5000:5000 anpr-system
```
Now, access [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

---

## 🚀 Deploy on AWS EC2

### 1️⃣ Launch Ubuntu EC2 Instance

### 2️⃣ Install Docker on EC2
```bash
sudo apt update && sudo apt install -y docker.io
```

### 3️⃣ Transfer Files to EC2
```bash
scp -i your-key.pem -r ANPR_Project ubuntu@your-ec2-ip:~/
```

### 4️⃣ Run the Docker Container
```bash
docker run -d -p 80:5000 anpr-system
```

### 5️⃣ Access the ANPR System
Open [http://your-ec2-ip/](http://your-ec2-ip/) in your browser.

---

## 📝 Logging & Storage
- Detected plates are logged in `detections_log.csv` with timestamps.
- The last 5 detections are displayed on the UI.

---

## 📜 License
This project is licensed under [MIT License](LICENSE).


---

## 📬 Contact
For any issues or contributions, please open an issue on GitHub or reach out via email.

---


