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

# Fill the screen with a color (e.g., red in RGB565 format)
display.fill_screen(0xF800)  # Red color
