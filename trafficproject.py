from os import fdopen
import cv2
import numpy as np
import math
from object_detection import ObjectDetection
import os

linePoints = []
trafficPoint = []


def lineCrossed(line1, line2, p):
    isCrossed = False

    a = math.sqrt((line2[0] - line1[0]) ** 2 + (line2[1] - line1[1]) ** 2)
    b = math.sqrt((line2[0] - p[0]) ** 2 + (line2[1] - p[1]) ** 2)
    c = math.sqrt((p[0] - line1[0]) ** 2 + (p[1] - line1[1]) ** 2)

    cosalfa = (a ** 2 + c ** 2 - b ** 2) / (2 * a * c)
    alfa = math.acos(cosalfa)

    distance = b * math.sin(alfa)

    if (distance < 15):
        isCrossed = True

    return isCrossed


# --------------------------------------------------------------------------------

def badCheck(object_id):
    for ob in bad_objects:
        if ob == object_id:
            return True

    return False


def saveInfraction(id, time, location, image):
    cv2.imwrite("Results/infraction%d.jpg" % id, image)


# --------------------------------------------------------------------------------

def drawLine(event, x, y, flags, par):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('check')
        linePoints.append([x, y])
        cv2.circle(frame, (x, y), 3, (0, 255, 0), 3)
        cv2.imshow("Frame", frame)


# -------------------------------------------------------------------------------
def drawPoint(event, x, y, flags, par):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('check')
        trafficPoint.append([x, y])
        cv2.circle(frame, (x, y), 5, (25, 25, 25), 3)
        cv2.imshow("Frame", frame)


# --------------------------------------------------------------------------------


od = ObjectDetection()
cap = cv2.VideoCapture("video1.mkv")
count = 0
center_points_prev_frame = []

tracking_objects = {}
track_id = 0
objects = []

# Objekti, kas parkapusi noteikumus
bad_objects = []
bad_count = 0

while True:

    ret, frame = cap.read()
    hsv_frame_temp = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hsv_frame = cv2.cvtColor(hsv_frame_temp, cv2.COLOR_RGB2HSV)
    cv2.imshow("Frame", frame)

    if count < 1:
        while len(linePoints) < 2:
            if (len(linePoints) < 1):
                cv2.rectangle(frame, (0, 0), (700, 120), (255, 255, 255), -1)
                cv2.putText(frame, 'Set 1st point', (0, 100), 0, 3, (50, 200, 50), 3)
                cv2.imshow("Frame", frame)
            elif (len(linePoints) < 2):
                cv2.rectangle(frame, (0, 0), (700, 120), (255, 255, 255), -1)
                cv2.putText(frame, 'Set 2nd point', (0, 100), 0, 3, (50, 200, 50), 3)
                cv2.imshow("Frame", frame)
            cv2.setMouseCallback("Frame", drawLine)
            cv2.imshow("Frame", frame)
            cv2.waitKey(100)

    if count < 1:
        while len(trafficPoint) < 1:
            cv2.rectangle(frame, (0, 0), (700, 120), (255, 255, 255), -1)
            cv2.putText(frame, 'Set traffic light', (0, 100), 0, 3, (50, 200, 50), 3)
            cv2.setMouseCallback("Frame", drawPoint)
            cv2.imshow("Frame", frame)
            cv2.waitKey(100)

    count += 1
    if not ret:
        break

    image = frame
    center_points_cur_frame = []
    width = int(cap.get(3))
    height = int(cap.get(4))
    height2, width2, _ = frame.shape

    cx = int(width2 * 23.9 / 32.5)
    cy = int(height2 * 10.2 / 18.4)

    (cx, cy) = trafficPoint[0]
    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    color = "Undefined"
    if g > 100:
        color = "RED"
    else:
        color = "BLACK"

    cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
    cv2.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 5)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
    (class_ids, scores, boxes) = od.detect(frame)

    for box in boxes:
        (x, y, w, h) = box
        cx = int((x + x + w) / 2)
        cy = int((y + y + h) / 2)
        center_points_cur_frame.append((cx, cy))
        print("FRAME #", count, " ", x, y, w, h)
        #  cv2.circle(frame, (cx,cy),5,(0,0,255), -1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if count <= 2:
        for pt in center_points_cur_frame:
            for pt2 in center_points_prev_frame:
                distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])

                if distance < 20:
                    tracking_objects[track_id] = pt
                    track_id += 1
    else:

        tracking_objects_copy = tracking_objects.copy()
        center_points_cur_frame_copy = center_points_cur_frame.copy()

        for object_id, pt2 in tracking_objects_copy.items():
            object_exits = False

            for pt in center_points_cur_frame_copy:
                distance = math.hypot(pt2[0] - pt[0], pt2[1] - pt[1])

                if distance < 20:
                    tracking_objects[object_id] = pt
                    object_exits = True
                    if pt in center_points_cur_frame:
                        center_points_cur_frame.remove(pt)
                    continue

            if not object_exits:
                tracking_objects.pop(object_id)

        for pt in center_points_cur_frame:
            tracking_objects[track_id] = pt
            track_id += 1

    for object_id, pt in tracking_objects.items():
        cv2.circle(frame, pt, 5, (0, 0, 255), -1)
        cv2.putText(frame, str(object_id), (pt[0], pt[1] - 7), 0, 1, (0, 0, 255), 1)

    lineA = linePoints[0]
    lineB = linePoints[1]
    zone = cv2.line(frame, lineA, lineB, (255, 0, 0), 4)

    cv2.imshow("Frame", frame)

    if color == "RED":

        for object_id, pt in tracking_objects.items():

            if badCheck(object_id) == True:
                continue

            if lineCrossed(lineA, lineB, pt) == True:
                bad_objects.append(object_id)
                bad_count += 1
                saveInfraction(object_id, 1, 1, image)
                print(object_id)

    print(bad_count)
    objects.clear()

    center_points_prev_frame = center_points_cur_frame.copy()

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()