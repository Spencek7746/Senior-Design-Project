import cv2
import numpy as np
from ultralytics import YOLO

#model = YOLO('yolov8n.pt')

def trainModel():
   results = model.train(
       data = r'../Data/data.yaml',
       imgsz = 640,
       epochs = 250,
       batch = 8,
       name = 'test_model'
       ) 

def verifyModelVideo():
    video_path = r'../examples/example1.mp4'
    video_path_out = '{}_out.mp4'.format(video_path)

    video_capture = cv2.VideoCapture(video_path)
    ret, frame = video_capture.read()
    H, W, _ = frame.shape
    out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'mp4v'), int(video_capture.get(cv2.CAP_PROP_FPS)), (W, H))

    model = YOLO(r'../runs/detect/test_model250/weights/best.pt')
    threshold = 0.5

    class_name_dict = {0: 'Empty',
                       1: 'Taken'}

    while ret:
        results = model(frame)[0]

        for result in results.boxes.data.tolist():
            x1,y1, x2, y2, score, class_id = result

            if score > threshold:
                if class_id == 0:  
                    color = (0, 255, 0) 
                elif class_id == 1: 
                    color = (0, 0, 255) 
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 4)
                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 1.3, color, 3, cv2.LINE_AA)

        out.write(frame)
        ret, frame = video_capture.read()

def verifyModel():
    model = YOLO(r'../runs/detect/test_model250/weights/best.pt')

    image_path = r'../examples/exampleImg.jpg'
    image = cv2.imread(r'../examples/exampleImg.jpg')

    results = model(r'../examples/exampleImg.jpg')


    threshold = 0.5

#verifyModel()
verifyModelVideo()
