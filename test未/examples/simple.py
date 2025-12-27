"""
このプログラムはTelloを制御するシンプルなスクリプトです。
実行内容：
1. Telloと接続
2. 離陸 (Takeoff)
3. 左へ100cm移動
4. 時計回りに90度回転
5. 前へ100cm移動
6. 着陸 (Land)

使用パッケージ:
- djitellopy: Telloドローン制御用ライブラリ
"""
from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_left(100)
tello.rotate_clockwise(90)
tello.move_forward(100)

tello.land()