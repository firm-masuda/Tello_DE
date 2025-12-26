from djitellopy import Tello

def main():
    # Initialize Tello
    tello = Tello()

    # Connect to the drone
    tello.connect()
    print(f"Battery: {tello.get_battery()}%")

    # Takeoff
    tello.takeoff()

    # Rotate 90 degrees clockwise
    tello.rotate_clockwise(90)

    # Land
    tello.land()

if __name__ == "__main__":
    main()
