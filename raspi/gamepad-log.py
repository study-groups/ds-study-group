import time
import pygame
import RPi.GPIO as GPIO
import math

# Initialize GPIO pin 21 for PWM output
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
led = GPIO.PWM(21, 100)
led.start(0)

# Initialize Pygame and the game controller
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Define some constants for mapping the controller input to LED brightness
MIN_BRIGHTNESS = 0
MAX_BRIGHTNESS = 100
AXIS_INDEX = 2  # The controller axis to use for controlling the LED
AXIS_MIN = -1.0  # The minimum value of the controller axis
AXIS_MAX = 1.0  # The maximum value of the controller axis
LOG_BASE = 2  # The base of the logarithmic function

try:
    while True:
        # Get the latest events from Pygame
        pygame.event.pump()

        # Read the value of the controller axis that controls the LED
        axis_value = joystick.get_axis(AXIS_INDEX)

        # Map the controller input to LED brightness using a logarithmic function
        brightness = int((math.log(abs(axis_value) + 1, LOG_BASE) / math.log(AXIS_MAX + 1, LOG_BASE)) * (MAX_BRIGHTNESS - MIN_BRIGHTNESS) + MIN_BRIGHTNESS)
        if axis_value < 0:
            brightness *= -1

        # Set the brightness of the LED using PWM
        led.ChangeDutyCycle(brightness)

        # Wait for a short amount of time before repeating
        time.sleep(0.01)

except KeyboardInterrupt:
    # Clean up the GPIO pin and Pygame
    led.stop()
    GPIO.cleanup()
    pygame.quit()

