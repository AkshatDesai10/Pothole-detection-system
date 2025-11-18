import cv2
from ultralytics import YOLO
from tkinter import Tk, filedialog
import os


model = YOLO("runs/detect/train/weights/best.pt") 


root = Tk()
root.withdraw()
image_path = filedialog.askopenfilename(title="Select an Image")

if image_path:
    results = model(image_path)  
    result_image = results[0].plot()

    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

   
    filename = os.path.basename(image_path)
    output_path = os.path.join(output_dir, f"detected_{filename}")

    cv2.imwrite(output_path, result_image)
    print(f"✅ Detection completed. Output saved at: {output_path}")

    
    cv2.imshow("Pothole Detection", result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("❌ No image selected")
