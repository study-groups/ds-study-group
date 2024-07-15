import cv2
import numpy as np
import time
import hid
import sounddevice as sd

# Define some constants for drawing circles on the image
GREEN = (0, 255, 0)  # The color of the circles (in BGR format)
THUMB_RADIUS = 30  # The radius of the thumb circle
OTHER_RADIUS = 15  # The radius of the index/middle finger circles

# Define some constants for audio generation
SAMPLE_RATE = 48000  # The sample rate of the audio signal
DURATION = 0.1  # The duration of each audio buffer (in seconds)
VOLUME = 0.1  # The starting volume (as a fraction of max)
MAX_VOLUME = 1.0  # The maximum volume (as a fraction of max)
MIN_VOLUME = 0.001  # The minimum volume (as a fraction of max)
VOLUME_STEP = 0.5  # The amount to increase/decrease the volume by when a button is pressed
MIN_FREQUENCY = 40  # Minimum frequency for the sine wave
MAX_FREQUENCY = 180  # Maximum frequency for the sine wave

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
        return None

    print(f"Connected to gamepad: {gamepad.get_product_string()}")
    return gamepad

def draw_circle(img, center, radius, color):
    cv2.circle(img, center, radius, color, -1)

def detect_finger_tip(img, threshold):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply a Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)

    # Apply thresholding to create a binary image
    _, thresh = cv2.threshold(blurred, threshold, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        # Find the contour with the largest area (assumes that the finger is the largest contour)
        largest_contour = max(contours, key=cv2.contourArea)

        # Find the tip of the finger by finding the point in the contour with the smallest y-coordinate
        tip = tuple(largest_contour[largest_contour[:,:,1].argmin()][0])
    else:
        # If no contours were found, return a point at the center of the image
        tip = (img.shape[1] // 2, img.shape[0] // 2)

    return tip

def list_camera_devices():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr

def list_audio_devices():
    devices = sd.query_devices()
    output_devices = [device for device in devices if device['max_output_channels'] > 0]
    return output_devices

def main():
    global VOLUME  # Declare global VOLUME at the start of the function
    print("Listing all HID devices:")
    list_hid_devices()
    print("\nReading from gamepad:")
    gamepad = read_gamepad()
    if not gamepad:
        return

    print("Listing all camera devices:")
    cameras = list_camera_devices()
    if not cameras:
        print("No camera devices found.")
        return

    print("Available camera devices:")
    for i, cam in enumerate(cameras):
        print(f"{i}: Camera {cam}")

    cam_index = int(input("Select the camera index to use: "))
    if cam_index < 0 or cam_index >= len(cameras):
        print("Invalid camera index selected.")
        return

    cap = cv2.VideoCapture(cameras[cam_index])

    print("Listing all audio output devices:")
    audio_devices = list_audio_devices()
    if not audio_devices:
        print("No audio output devices found.")
        return

    print("Available audio output devices:")
    for i, device in enumerate(audio_devices):
        print(f"{i}: {device['name']}")

    audio_index = input("Select the audio output device index to use (or press Enter to skip): ")
    if audio_index:
        audio_index = int(audio_index)
        if audio_index < 0 or audio_index >= len(audio_devices):
            print("Invalid audio output device index selected.")
            return
        sd.default.device = audio_devices[audio_index]['name']
    else:
        print("No audio output device selected. Continuing without audio.")

    try:
        while True:
            # Capture a frame from the video device
            ret, frame = cap.read()
            if not ret:
                break

            # Flip the frame horizontally (mirror effect)
            frame = cv2.flip(frame, 1)

            # Detect the tips of the fingers
            thumb_tip = detect_finger_tip(frame, 150)
            index_tip = detect_finger_tip(frame, 50)
            middle_tip = detect_finger_tip(frame, 70)

            # Draw circles on the frame
            draw_circle(frame, thumb_tip, THUMB_RADIUS * 2, GREEN)
            draw_circle(frame, index_tip, OTHER_RADIUS, GREEN)
            draw_circle(frame, middle_tip, OTHER_RADIUS, GREEN)

            # Calculate frequency based on the y-coordinate of the thumb tip
            y = thumb_tip[1]
            height = frame.shape[0]
            frequency = MIN_FREQUENCY + (MAX_FREQUENCY - MIN_FREQUENCY) * (height - y) / height

            # Generate and play sound if an audio device is selected
            if audio_index:
                samples = (VOLUME * np.sin(2 * np.pi * np.arange(SAMPLE_RATE * DURATION) * frequency / SAMPLE_RATE)).astype(np.float32)
                sd.play(samples, samplerate=SAMPLE_RATE)

            # Read gamepad report
            report = gamepad.read(64)
            if report:
                print("Report: ", report)
                # Update the volume based on the gamepad input
                if report[0] == 3:  # Assuming button 3 increases volume
                    VOLUME = min(VOLUME * 2 ** (0.5/20), MAX_VOLUME)
                elif report[0] == 2:  # Assuming button 2 decreases volume
                    VOLUME = max(VOLUME * 2 ** (-0.5/20), MIN_VOLUME)

            # Display the frame
            cv2.imshow('Frame', frame)

            # Check if the 'q' key was pressed to quit the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            time.sleep(0.01)
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        gamepad.close()
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
