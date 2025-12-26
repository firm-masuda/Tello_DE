from djitellopy import Tello
import cv2
import time

def main():
    # Telloオブジェクトの作成
    tello = Tello()

    # Telloに接続
    print("Telloに接続中...")
    try:
        tello.connect()
    except Exception as e:
        print(f"接続に失敗しました: {e}")
        return

    # バッテリー残量の表示
    print(f"バッテリー残量: {tello.get_battery()}%")

    # カメラストリーミングを開始
    tello.streamon()
    
    # ストリームが安定するまで軽く待機
    time.sleep(1)

    print("動画ストリーミングを開始します。画面上のウィンドウを選択して 'q' キーを押すと終了します。")

    # フレーム読み取りオブジェクトを取得
    frame_reader = tello.get_frame_read()

    try:
        while True:
            # 最新のフレームを取得
            frame = frame_reader.frame

            # フレームが取得できていない場合はスキップ
            if frame is None:
                continue

            # djitellopyはRGB形式で画像を返すため、OpenCV用にBGRに変換
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            # 画像を表示
            cv2.imshow('Tello Camera', frame)

            # 'q' キーで終了
            # waitKey(1) は1ミリ秒キー入力を待つ
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    except KeyboardInterrupt:
        print("ユーザーによる中断")
    except Exception as e:
        print(f"エラーが発生しました: {e}")
    finally:
        # リソースの解放
        print("終了処理中...")
        tello.streamoff()
        cv2.destroyAllWindows()
        print("終了しました。")

if __name__ == "__main__":
    main()
