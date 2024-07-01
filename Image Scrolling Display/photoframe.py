import pygame
from time import sleep

pygame.init()

WIDTH = 1280
HEIGHT = 1080
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 0)

# pygame.FULLSCREEN
List = ["1.jpg"]
count = 0
while True:

    for x in List:
        windowSurface.fill((255,255,255))
        img = pygame.image.load(x)

        windowSurface.blit(img, (0, 0))

        pygame.display.update()
        sleep(3)



"""
import Adafruit_DHT

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT11

# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
#pin = 'P8_11'

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO4.
pin = 4

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
"""