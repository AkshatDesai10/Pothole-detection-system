import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tkinter import filedialog, Tk

Tk().withdraw()

model = load_model("pothole_model.h5")
categories = ["normal", "pothole"]

custom_labels = {"normal": "Normal Road", "pothole": "Pothole Detected"}
label_colors = {"normal": (0, 255, 0), "pothole": (0, 0, 255)} 

def predict_and_show(img_path):
   
    img = cv2.imread(img_path)
    img_resized = cv2.resize(img, (128, 128))
    img_input = img_resized / 255.0
    img_input = img_input.reshape(1, 128, 128, 3)
    
   
    pred = model.predict(img_input)[0]
    label = categories[np.argmax(pred)]
    
 
    display_img = cv2.resize(img, (400, 400))
    color = label_colors[label]
    
    cv2.putText(display_img, f"{custom_labels[label]}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    cv2.imshow("Pothole Detection", display_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
   
    print("Predicted:", custom_labels[label])
predict_and_show(filedialog.askopenfilename())
