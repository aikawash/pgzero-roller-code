from rpi_ws281x import *
import time

# LED strip configuration:
LED_COUNT      = 36      # Number of LED pixels.
LED_PIN        = 12      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 150     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ,LED_DMA,LED_INVERT,LED_BRIGHTNESS,LED_CHANNEL)
strip.begin()

while True:
    for x in range(0,9):
        strip.setPixelColor(x,Color(245,40,0))
        strip.setPixelColor(x+18,Color(245,40,0))
        strip.setPixelColor(17-x,Color(245,40,0))
        strip.setPixelColor(35-x,Color(245,40,0))
        strip.show()
        print(x)
        time.sleep(0.3)
        strip.setPixelColor(x,Color(0,0,0))
        strip.setPixelColor(x+18,Color(0,0,0))
        strip.setPixelColor(17-x,Color(0,0,0))
        strip.setPixelColor(35-x,Color(0,0,0))
        strip.show()
        #time.sleep(1)




#for x in range(0,LED_COUNT):
    