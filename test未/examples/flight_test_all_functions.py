"""
このプログラムはTelloの様々なSDKコマンド（状態取得、設定、移動、フリップなど）を網羅的にテストするスクリプトです。
各機能の動作確認やデバッグに使用します。

使用パッケージ:
- djitellopy: Telloドローン制御用ライブラリ
"""
from djitellopy import Tello

tello = Tello()

# connect commands
tello.connect()

# takeoff commands
tello.takeoff()

print('get & query commands 1st. ----------------------------------------------------------')
# get commands
print('get_acceleration_x:',tello.get_acceleration_x())
print('get_acceleration_y:',tello.get_acceleration_y())
print('get_acceleration_z:',tello.get_acceleration_z())
print('get_barometer:',tello.get_barometer())
print('get_get_battery:',tello.get_battery())
print('get_current_state:',tello.get_current_state())
print('get_distance_tof:',tello.get_distance_tof())
print('get_flight_time:',tello.get_flight_time())
# print('get_acceleration_x:',tello.get_frame_read()) 他のプログラムでテスト
print('get_height:',tello.get_height())
print('get_highest_temperature:',tello.get_highest_temperature())
print('get_lowest_temperature:',tello.get_lowest_temperature())
# print('get_mission_pad_distance_x:',tello.get_mission_pad_distance_x()) # SDK2.0
# print('get_mission_pad_distance_y:',tello.get_mission_pad_distance_y()) # SDK2.0
# print('get_mission_pad_distance_z:',tello.get_mission_pad_distance_z()) # SDK2.0
# print('get_mission_pad_id():',tello.get_mission_pad_id()) # SDK2.0
# print('get_own_udp_object:',tello.get_own_udp_object()) # 通常自分自身では使わない
print('get_pitch:',tello.get_pitch())
print('get_roll:',tello.get_roll())
print('get_speed_x:',tello.get_speed_x())
print('get_speed_y:',tello.get_speed_y())
print('get_speed_z:',tello.get_speed_z())
# print('get_state_fiel:',tello.get_state_field()) # 通常自分自身では使わない
print('get_temperature:',tello.get_temperature())
# print('get_udp_video_address:',tello.get_udp_video_address())
# print('get_video_capture:',tello.get_video_capture())
print('get_yaw:',tello.get_yaw())

# query commands
print('query_attitude:',tello.query_attitude())
# print('query_barometer:',tello.query_barometer())   # Bug?
print('query_battery:',tello.query_battery())
print('query_distance_tof:',tello.query_distance_tof())
# print('query_flight_time:',tello.query_flight_time())  # Bug?
# print('query_height:',tello.query_height())  # Bug?
# print('query_sdk_version:',tello.query_sdk_version()) # SDK2.0
# print('query_serial_number:',tello.query_serial_number())  # SDK2.0
# print('query_speed:',tello.query_speed())  # Bug?
# print('query_temperature:',tello.query_temperature()) # Bug?
print('query_wifi_signal_noise_ratio:',tello.query_wifi_signal_noise_ratio())

# UP 20cm,rotate cw 90
tello.move_up(20)
tello.rotate_clockwise(90)

# emergency
# tello.emergency() テスト時にコメントアウトを消す

print('get & query commands 2st. ----------------------------------------------------------')
# get commands
print('get_acceleration_x:',tello.get_acceleration_x())
print('get_acceleration_y:',tello.get_acceleration_y())
print('get_acceleration_z:',tello.get_acceleration_z())
print('get_barometer:',tello.get_barometer())
print('get_get_battery:',tello.get_battery())
print('get_current_state:',tello.get_current_state())
print('get_distance_tof:',tello.get_distance_tof())
print('get_flight_time:',tello.get_flight_time())
# print('get_acceleration_x:',tello.get_frame_read()) 他のプログラムでテスト
print('get_height:',tello.get_height())
print('get_highest_temperature:',tello.get_highest_temperature())
print('get_lowest_temperature:',tello.get_lowest_temperature())
# print('get_mission_pad_distance_x:',tello.get_mission_pad_distance_x()) # SDK2.0
# print('get_mission_pad_distance_y:',tello.get_mission_pad_distance_y()) # SDK2.0
# print('get_mission_pad_distance_z:',tello.get_mission_pad_distance_z()) # SDK2.0
# print('get_mission_pad_id():',tello.get_mission_pad_id()) # SDK2.0
# print('get_own_udp_object:',tello.get_own_udp_object()) # 通常自分自身では使わない
print('get_pitch:',tello.get_pitch())
print('get_roll:',tello.get_roll())
print('get_speed_x:',tello.get_speed_x())
print('get_speed_y:',tello.get_speed_y())
print('get_speed_z:',tello.get_speed_z())
# print('get_state_fiel:',tello.get_state_field()) # 通常自分自身では使わない
print('get_temperature:',tello.get_temperature())
# print('get_udp_video_address:',tello.get_udp_video_address())
# print('get_video_capture:',tello.get_video_capture())
print('get_yaw:',tello.get_yaw())

# query commands
print('query_attitude:',tello.query_attitude())
# print('query_barometer:',tello.query_barometer())   # Bug?
print('query_battery:',tello.query_battery())
print('query_distance_tof:',tello.query_distance_tof())
# print('query_flight_time:',tello.query_flight_time())  # Bug?
# print('query_height:',tello.query_height())  # Bug?
# print('query_sdk_version:',tello.query_sdk_version()) # SDK2.0
# print('query_serial_number:',tello.query_serial_number())  # SDK2.0
# print('query_speed:',tello.query_speed())  # Bug?
# print('query_temperature:',tello.query_temperature()) # Bug?
print('query_wifi_signal_noise_ratio:',tello.query_wifi_signal_noise_ratio())

# move commands
print('move commands----------------------------------------------------------')
# tello.move('up',20) レスポンスは、OKが戻るが、以降のコマンドで異常発生
tello.move_left(20)
tello.move_right(20)
tello.move_up(20)
tello.move_down(20)
tello.move_forward(20)
tello.move_back(20)

# rotate commands
tello.rotate_clockwise(90)
tello.rotate_counter_clockwise(90)

# curve
tello.curve_xyz_speed(30,30,30,60,60,0,10)

tello.rotate_clockwise(180)

# set speed
tello.set_speed(30)

# curve
tello.curve_xyz_speed(30,30,30,60,60,0,10)

# rc
tello.send_rc_control()

# go
tello.curve_xyz_speed(30,30,30,20)

# flip commands
# tello.flip('l')
tello.flip_forward()
# tello.flip_back() フリップ失敗で落下の場合があるため正常に動くがコメントアウト
# tello.flip_left() フリップ失敗で落下の場合があるため正常に動くがコメントアウト
# tello.flip_right() フリップ失敗で落下の場合があるため正常に動くがコメントアウト

tello.land()