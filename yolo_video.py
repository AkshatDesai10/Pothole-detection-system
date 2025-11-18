import cv2
import os
from ultralytics import YOLO
from tkinter import Tk, filedialog

model = YOLO("runs/detect/train/weights/best.pt")

Tk().withdraw()

video_path = filedialog.askopenfilename(title="Select a Video", filetypes=[("Video files", "*.mp4;*.avi;*.mov")])

if video_path:
 
    output_folder = "output_videos"
    os.makedirs(output_folder, exist_ok=True)

  
    output_path = os.path.join(output_folder, "output_video.mp4")

    cap = cv2.VideoCapture(video_path)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

      
        results = model(frame)

        annotated_frame = results[0].plot()

        out.write(annotated_frame)

    cap.release()
    out.release()
    print(f"✅ Video detection complete! Output saved at {output_path}")

else:
    print("❌ No video selected.")
