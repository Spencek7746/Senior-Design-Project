import cv2
import numpy as np
from roboflow import Roboflow
from ultralytics import YOLO

model = YOLO('yolov8n.yaml')

model.train(data=r'.\Data\data.yaml', epochs=100, imgsz=640)



