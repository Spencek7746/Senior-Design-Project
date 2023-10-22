import sys
import logging
import cv2
import numpy as np
from ultralytics import YOLO

def verifyModel():
# redirect output so it can actually be captured
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    model = YOLO(r'../runs/detect/test_model250/weights/best.pt')

    image_path = r'./test.jpg'
#    image_path = r'../examples/exampleImg4.jpg'
    image = cv2.imread(image_path)

    threshold = 0.5;

    results = model.predict(image, conf=threshold)[0]

    class_name_dict = {0: 'Empty',
                       1: 'Taken'}

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)
        class_id = int(class_id)

        if score > threshold:
            if class_id == 0:  
                color = (0, 255, 0) 
            elif class_id == 1: 
                color = (0, 0, 255) 

        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), color, 4)
        cv2.putText(image, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 1.3, color, 3, cv2.LINE_AA)

    cv2.imwrite("./processed.jpg", image)

verifyModel()
#verifyModelVideo()
