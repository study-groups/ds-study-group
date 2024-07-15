import hid
import time

def list_hid_devices():
    for device in hid.enumerate():
        keys = list(device.keys())
        keys.sort()
        for key in keys:
            print(f"{key}: {device[key]}")
        print()

def read_gamepad():
    gamepad = None
    for device in hid.enumerate():
        if device['vendor_id'] == 0x2dc8 and device['product_id'] == 0x6101:
            gamepad = hid.device()
            gamepad.open_path(device['path'])
            break

    if not gamepad:
        print("No gamepad detected. Please connect a gamepad and try again.")
        return

    print(f"Connected to gamepad: {gamepad.get_product_string()}")
    try:
        while True:
            report = gamepad.read(64)
            if report:
                print("Report: ", report)
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        gamepad.close()

if __name__ == "__main__":
    print("Listing all HID devices:")
    list_hid_devices()
    print("\nReading from gamepad:")
    read_gamepad()
