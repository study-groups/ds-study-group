import cv2
import numpy as np
import pygame
import sounddevice as sd

# Disable the video system to avoid errors
#pygame.display.set_mode((1, 1), pygame.NOFRAME)
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
cap = cv2.VideoCapture(0)

# Define a function to detect the tip of a finger in an image
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

def draw_circle(img, center, radius, color):
    cv2.circle(img, center, radius, color, -1)

# Define some constants for drawing circles on the image
GREEN = (0, 255, 0)  # The color of the circles (in BGR format)
THUMB_RADIUS = 30  # The radius of the thumb circle
OTHER_RADIUS = 15  # The radius of the index/middle finger circles
WINDOW_NAME = "Fingertips"
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
cv2.resizeWindow(WINDOW_NAME, WINDOW_WIDTH, WINDOW_HEIGHT)

# Define some constants for audio generation
SAMPLE_RATE = 48000  # The sample rate of the audio signal
DURATION = 0.1  # The duration of each audio buffer (in seconds)
FREQUENCY = 220  # The frequency of the audio tone (in Hz)
VOLUME = 0.1  # The starting volume (as a fraction of max)
MAX_VOLUME = 1.0  # The maximum volume (as a fraction of max)
MIN_VOLUME = 0.001  # The minimum volume (as a fraction of max)
VOLUME_STEP = 0.5  # The amount to increase/decrease the volume by when a button is pressed

# Define a generator function to generate the sine wave samples
def sine_wave_generator():
    while True:
        t = np.linspace(0, DURATION,
                int(DURATION * SAMPLE_RATE), endpoint=False)
        samples = VOLUME * np.sin(2 * np.pi * FREQUENCY * t)
        yield samples.astype(np.float32)

# Define the audio callback function
def audio_callback(outdata, frames, time, status):
    samples = sine_wave_generator().__next__()
    outdata[:] = np.repeat(samples.reshape((-1, 1)), 2, axis=1)

# Initialize the video capture device (use 0 for the default camera)

# Start the audio stream
with sd.OutputStream(channels=2, blocksize=int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, callback=audio_callback):
    # Initialize Pygame and the game controller

    # Start the video capture loop
    while True:
        _, frame = cap.read()
        # Break out of loop if no frame was captured
        if frame is None:
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
        cv2.imshow(WINDOW_NAME, frame)

        cv2.waitKey(1)


        # Check for gamepad events and print them to the console
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                print(f"Joystick axis motion: axis={event.axis}, value={event.value}")
            elif event.type == pygame.JOYBUTTONDOWN:
                print(f"Joystick button down: button={event.button}")
            elif event.type == pygame.JOYBUTTONUP:
                print(f"Joystick button up: button={event.button}")

        # Update the volume based on the gamepad input
        if joystick.get_button(3):  # Check if the volume up button is pressed
            VOLUME = min(VOLUME * 2 ** (0.5/20), MAX_VOLUME)
        elif joystick.get_button(2):  # Check if the volume down button is pressed
            VOLUME = max(VOLUME * 2 ** (-0.5/20), MIN_VOLUME)


        # Wait for a short time to avoid consuming too much CPU
        pygame.time.wait(10)

cap.release()

pygame.quit()
