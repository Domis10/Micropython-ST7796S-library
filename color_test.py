import machine
import st7796s
from machine import Pin, SPI

# Initialize SPI
spi = SPI(0, baudrate=40000000, sck=Pin(18), mosi=Pin(19))

# Initialize the control pins
cs = Pin(17, Pin.OUT)
dc = Pin(16, Pin.OUT)
rst = Pin(22, Pin.OUT)

# Initialize the display
display = st7796s.ST7796S(spi, dc, rst, cs)

# Set rotation (0: Portrait, 1: Landscape, 2: Portrait upside down, 3: Landscape upside down)
display.set_rotation(1)  # Landscape mode

# Fill the screen with a color (e.g., red in RGB565 format)
display.fill_screen(0xF800)  # Red color
