import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

def trainModel():
   results = model.train(
       data = r'.\Data\data.yaml',
       imgsz = 640,
       epochs = 250,
       batch = 8,
       name = 'test_model'
       ) 

trainModel()