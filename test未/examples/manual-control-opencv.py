"""
このプログラムはキーボードを使ってTelloを制御するシンプルなスクリプトです。
より機能が充実した例については manual-control-pygame.py を参照してください。

操作方法:
- W, A, S, D: 前後左右移動
- E, Q: 時計回りと反時計回りの回転
- R, F: 上昇と下降
- ESC: 着陸してプログラム終了

使用パッケージ:
- djitellopy: Telloドローン制御用ライブラリ
- cv2 (OpenCV): 画像処理、キーボード入力取得用
- math: 数学関数（※このスクリプトでは未使用）
- time: 待機処理用
"""

from djitellopy import Tello
import cv2, math, time

tello = Tello()
tello.connect()

tello.streamon()
frame_read = tello.get_frame_read()

tello.takeoff()

while True:
    # 実際には、フレーム表示を別スレッドで行う必要があります。
    # そうしないと、ドローンが移動している間、映像がフリーズします。
    img = frame_read.frame
    cv2.imshow("drone", img)

    key = cv2.waitKey(1) & 0xff
    if key == 27: # ESC
        break
    elif key == ord('w'):
        tello.move_forward(30)
    elif key == ord('s'):
        tello.move_back(30)
    elif key == ord('a'):
        tello.move_left(30)
    elif key == ord('d'):
        tello.move_right(30)
    elif key == ord('e'):
        tello.rotate_clockwise(30)
    elif key == ord('q'):
        tello.rotate_counter_clockwise(30)
    elif key == ord('r'):
        tello.move_up(30)
    elif key == ord('f'):
        tello.move_down(30)

tello.land()
