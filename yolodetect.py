from ultralytics import YOLO
import cv2
import numpy as np
import time
from telegram_utils import send_telegram
import datetime
import threading
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

def isInside(points, centroid):
    polygon = Polygon(points)
    centroid = Point(centroid)
    print(polygon.contains(centroid))
    return polygon.contains(centroid)


class YoloDetect():
    def __init__(self, detect_class="person", frame_width=1280, frame_height=720):
        # Parameters
        self.model_file = "yolov8n.pt"  # YOLOv8 pre-trained model
        self.conf_threshold = 0.5
        self.detect_class = detect_class
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.model = YOLO(self.model_file)  # Load the YOLOv8 model
        self.last_alert = None
        self.alert_telegram_each = 5  # seconds

    def detect(self, frame, points):
        """
        Detect objects in a given frame inside the area defined by the points.
        Points are a list of (x, y) coordinates that define a polygon.
        """
        # Perform inference using YOLOv8
        results = self.model.predict(frame, conf=self.conf_threshold, verbose=False)
        
        # Process results
        detections = []
        for result in results[0].boxes.data.tolist():  # Iterate through detected objects
            x1, y1, x2, y2, confidence, class_id = result
            class_name = self.model.names[int(class_id)]  # Map class ID to class name
            
            # Check if the detected class matches the target
            if class_name == self.detect_class:
                # Check if the detection is inside the polygon defined by points
                detection_box = np.array([[(x1, y1), (x2, y2)]], dtype=np.int32)
                polygon = np.array([points], dtype=np.int32)

                # Check if the center of the bounding box is inside the polygon
                center_x = (x1 + x2) / 2
                center_y = (y1 + y2) / 2
                if cv2.pointPolygonTest(polygon, (center_x, center_y), False) >= 0:
                    detections.append({
                        "class": class_name,
                        "confidence": confidence,
                        "box": (int(x1), int(y1), int(x2), int(y2))
                    })

        return detections

    def draw_detections(self, frame, detections, points):
        """
        Draw bounding boxes and labels on the frame.
        """
        color = (0, 255, 0)
        for detection in detections:
            x1, y1, x2, y2 = detection["box"]
            label = f'{detection["class"]}: {detection["confidence"]:.2f}'
            # Draw bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Draw label
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            # Tinh toan centroid
            centroid = ((x1 + x2) // 2, (y1 + y2) // 2)
            cv2.circle(frame, centroid, 5, (color), -1)

            if isInside(points, centroid):
                self.alert(frame)
        return frame

    def alert(self, img):
        cv2.putText(img, "ALARM!!!!", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        # New thread to send telegram after 15 seconds
        if (self.last_alert is None) or (
                (datetime.datetime.utcnow() - self.last_alert).total_seconds() > self.alert_telegram_each):
            self.last_alert = datetime.datetime.utcnow()
            cv2.imwrite("alert.png", cv2.resize(img, dsize=None, fx=0.2, fy=0.2))
            thread = threading.Thread(target=send_telegram)
            thread.start()
        return img