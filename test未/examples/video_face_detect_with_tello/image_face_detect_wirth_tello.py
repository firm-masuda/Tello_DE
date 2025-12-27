"""
このプログラムはTelloのカメラ映像から顔と目を検出し、枠で囲んで表示するサンプルです。
Haar Cascade分類器（haarcascade_frontalface_default.xml, haarcascade_eye.xml）を使用します。

使用パッケージ:
- djitellopy: Telloドローン制御用ライブラリ
- cv2 (OpenCV): 映像取得、顔・目検出、描画、表示用
- math: 数学関数（※このスクリプトでは未使用）
- time: 待機処理（※このスクリプトでは未使用）
"""
from djitellopy import Tello
import cv2 as cv
import math,time

# cap = cv.VideoCapture(0)

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

# tello.takeoff()

while True:
    frame = frame_read.frame
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(len(faces))

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        eye_gray = gray[y:y+h, x:x+w]
        eye_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(eye_gray)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(eye_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
