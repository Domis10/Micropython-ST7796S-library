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

# Load image data from .bin file
def load_image_bin(filename):
    with open(filename, "rb") as f:
        return f.read()

# Display the image
image_file = "image.bin"  # Path to your .bin file
image_data = load_image_bin(image_file)

# Assuming the image is 320x480 (adjust dimensions as needed)
image_width = 480
image_height = 320

# Draw the image at position (0, 0)
display.draw_image(0, 0, image_width, image_height, image_data)
