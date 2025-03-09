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

# Function to stream and display image data
def display_image_bin(filename, x, y):
    # Open the .bin file
    with open(filename, "rb") as f:
        # Set the display window to the image dimensions (using the display's width and height)
        display.set_window(x, y, x + display.width - 1, y + display.height - 1)
        
        # Read and display the image in chunks
        chunk_size = 512  # Adjust this value based on available memory
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break  # End of file
            for i in range(0, len(chunk), 2):
                # Combine two bytes into a 16-bit RGB565 pixel
                pixel = (chunk[i] << 8) | chunk[i + 1]
                display.write_data_16bit(pixel)

# Display the image
image_file = "image.bin"  # Path to your .bin file

# Draw the image at position (0, 0)
display_image_bin(image_file, 0, 0)
