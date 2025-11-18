🚧 Pothole Detection Using YOLOv8

A computer vision project that automatically detects potholes from road images and videos using the YOLOv8 deep learning model. This project helps identify damaged road surfaces using object detection techniques and can be integrated into smart city or road maintenance applications.

📁 Project Structure
pothole-detection/
│
├── dataset/
├── train/
├── test/
├── valid/
├── data.yaml
│
├── pothole_detection.ipynb
├── predict.py
├── yolo_video.py
├── trial.py
│
├── pothole_model.h5
├── yolov8n.pt
│
├── runs/                 # YOLO training results
├── testroad1.jpg
├── testroad2.png
│
├── README.md

🧠 Model Used

This project uses:

✔ YOLOv8 (Ultralytics)

A state-of-the-art object detection model with real-time performance.

✔ Optional: TensorFlow .h5 Model

Included for experimental comparison (not required to run YOLO model).

🔧 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/pothole-detection.git
cd pothole-detection

2️⃣ Install Dependencies
pip install ultralytics opencv-python numpy matplotlib


If using TensorFlow model:

pip install tensorflow keras

3️⃣ Verify Dataset YAML

data.yaml must contain dataset paths and classes:

train: train/images
val: valid/images

names:
  0: pothole

🚀 How to Run the Project
✔ 1. Run Detection on Images
python predict.py


This script loads the YOLOv8 model and performs detection on test images (testroad1.jpg, testroad2.png).

✔ 2. Run Real-Time Detection using Webcam
python yolo_video.py


A window will open with live pothole detection from your system camera.

✔ 3. Run Notebook for Training / Analysis
jupyter notebook


Then open:

pothole_detection.ipynb

🏋️ Training YOLO Model (Optional)

If you want to retrain using your dataset:

yolo detect train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640


After training, the best model will be saved in:

runs/detect/train/weights/best.pt


To use the trained model, update predict.py.

📊 Results

YOLOv8 achieves:

High accuracy in detecting potholes

Real-time inference at >30 FPS (webcam)

Works for images and video footage

Inference images and training logs are stored inside the runs/ folder.

🎯 Features

Detects potholes in images, videos, and webcam feed

Works in real time

Supports custom training

Easy to integrate into mobile apps or IoT devices

Light & fast using YOLOv8n

🙌 Future Improvements

GPS tagging of detected potholes

Mobile app integration

Road condition severity scoring

Drone-based detection system

📄 License

This project is open-source and available under the MIT License.

🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to improve.

📬 Contact

For queries or improvements:

Akshat Desai
