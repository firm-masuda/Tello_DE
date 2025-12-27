"""
panoramaModule.py をインポートし、各関数を呼び出してパノラマ撮影を行うサンプルです。
panoramaModule.py で定義された関数を使用します。

使用パッケージ:
- djitellopy: Telloドローン制御用ライブラリ
- cv2 (OpenCV): 画像保存用 (モジュール内で使用)
- time: 待機処理用
- panoramaModule: パノラマ撮影ロジックを含む自作モジュール
"""
from djitellopy import Tello
import cv2
import time
import panoramaModule


tello = Tello()
tello.connect()

print(tello.get_battery())

tello.takeoff()
tello.move_up(500)
panoramaModule.panorama_half_clockwise(tello)
tello.land()
