import cv2
import numpy as np
from roboflow import Roboflow
from ultralytics import YOLO

model = YOLO('yolov8n.yaml')

model.train(data=r'C:\Users\karpa\source\repos\Senior-Design-Project\Data\data.yaml', epochs=100, imgsz=640)

