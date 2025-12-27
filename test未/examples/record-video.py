"""
このプログラムはTelloのカメラ映像を録画するスクリプトです。
実行内容：
1. Telloと接続
2. カメラ映像のストリーミング開始
3. 別スレッドで映像を 'video.avi' に保存
4. 離陸、上昇、回転、着陸
5. 録画終了

使用パッケージ:
- djitellopy: Telloドローン制御用ライブラリ
- cv2 (OpenCV): 映像の保存（VideoWriter）用
- time: 待機処理用
- threading: 映像保存処理を別スレッドで実行するため
"""
import time, cv2
from threading import Thread
from djitellopy import Tello

tello = Tello()

tello.connect()

keepRecording = True
tello.streamon()
frame_read = tello.get_frame_read()

def videoRecorder():
    # VideoWriteオブジェクトを作成し、./video.avi に記録する
    height, width, _ = frame_read.frame.shape
    video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (width, height))

    while keepRecording:
        video.write(frame_read.frame)
        time.sleep(1 / 30)

    video.release()

# 録画は別スレッドで実行する必要があります。そうしないと、ブロッキング操作により
# フレームがビデオに追加されなくなります
recorder = Thread(target=videoRecorder)
recorder.start()

tello.takeoff()
tello.move_up(100)
tello.rotate_counter_clockwise(360)
tello.land()

keepRecording = False
recorder.join()
