"""
このプログラムはTelloのカメラで写真を撮影するスクリプトです。
実行内容：
1. Telloと接続
2. カメラ映像のストリーミング開始
3. フレームを取得し 'picture.png' に保存
4. 離陸してから保存動作を行い
5. 着陸

使用パッケージ:
- djitellopy: Telloドローン制御用ライブラリ
- cv2 (OpenCV): 画像の保存（imwrite）用
"""
import cv2
from djitellopy import Tello

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()
cv2.imwrite("picture.png", frame_read.frame)

tello.land()
