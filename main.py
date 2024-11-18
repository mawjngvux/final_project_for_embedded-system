import cv2
import numpy as np
from imutils.video import VideoStream
from yolodetect import YoloDetect

def handle_left_click(event, x, y, flags, points):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append([x, y])

def draw_polygon (frame, points):
    for point in points:
        frame = cv2.circle( frame, (point[0], point[1]), 5, (0,0,255), -1)

    frame = cv2.polylines(frame, [np.int32(points)], False, (255,0, 0), thickness=2)
    return frame


video = VideoStream().start()
# video = VideoStream(src="http://192.168.1.87/").start()

detect = False
points = []
model = YoloDetect()

while True:
    frame = video.read()
    frame = cv2.flip(frame, 1)
    frame = draw_polygon(frame, points)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('d'):
        points.append(points[0])
        detect = True

    if detect:
        detections = model.detect(frame= frame, points= points)
        frame = model.draw_detections(frame, detections, points= points)

    cv2.imshow("Intrusion Warning", frame)

    cv2.setMouseCallback('Intrusion Warning', handle_left_click, points)

video.stop()
cv2.destroyAllWindows()