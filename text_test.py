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
# Initialize the display
display = st7796s.ST7796S(spi, dc, rst, cs)


text = "Test 1 2 3"  # Example text
x, y = 50, 50  # Starting position
text_color = 0xFFFF  # Text in white in RGB565
bg_color = 0x0000  # Background in black in RGB565

display.fill_screen(0x0000)
display.draw_text(x, y, text, text_color, bg_color)
