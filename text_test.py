import machine
import st7796s

# Initialize SPI and GPIO pins
spi = machine.SPI(1, baudrate=40000000, polarity=0, phase=0)
dc = machine.Pin(15, machine.Pin.OUT)
rst = machine.Pin(16, machine.Pin.OUT)
cs = machine.Pin(17, machine.Pin.OUT)

# Initialize the display
display = st7796s.ST7796S(spi, dc, rst, cs)

# Set rotation (0: Portrait, 1: Landscape, 2: Portrait upside down, 3: Landscape upside down)
display.set_rotation(1)  # Landscape mode

# Write text on the screen
text = "Test 1 2 3"  # Example text
x, y = 50, 50  # Starting position
text_color = 0xFFFF  # Text in white in RGB565
bg_color = 0x0000  # Background in black in RGB565

display.draw_text(x, y, text, text_color, bg_color)
