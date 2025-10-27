# detect.py
import torch
import cv2
from PIL import Image
import numpy as np

# Load pretrained YOLOv5s model from torch hub
def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    model.eval()
    return model

# Run inference and return annotated image + detections
def detect_objects(model, image_path):
    results = model(image_path)
    detections = results.pandas().xyxy[0]  # DataFrame of detections
    annotated = np.squeeze(results.render())  # Rendered image (numpy array)
    return annotated, detections
