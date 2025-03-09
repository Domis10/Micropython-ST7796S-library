# ST7796S MicroPython Library  

This repository contains a **MicroPython library** for interfacing with the **ST7796S** display. It includes example scripts for testing **colors**, **text**, and **images**, helping you quickly integrate the display into your MicroPython projects.  

## Features:  
- **Color Test**: Displays solid colors on the screen.  
- **Text Test**: Displays text on the screen.  
- **Image Conversion**: Converts an image to **RGB565 binary format** for display.  
- **Image Test**: Loads and displays a converted image on the screen.  
- **ST7796S Driver**: Handles display communication via SPI.  

## License & Usage  

You are free to **use, modify, and distribute** this code, but with the following conditions:  

1. **Attribution**:  
   - If you use this code in a **public project**, you must give credit to the original author (me).  
   - If you modify or build upon it, you must still acknowledge the original work.  

2. **Commercial Use**:  
   - If you use this code in a **commercial project**, you **must** give credit. This can be in the documentation, about page, or another appropriate section.  

3. **No Claim of Ownership**:  
   - You **cannot** claim this code as your own, even if you modify it.  

By using this code, you **agree** to these conditions.  

## Example Scripts  

### **1. Color Test (`color_test.py`)**  
This script fills the screen with a solid color.  

```python
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
```  

### **2. Text Test (`text_test.py`)**  
This script displays text on the screen.  

```python
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
text_color = 0xFFFF  # White text in RGB565
bg_color = 0x0000  # Black background in RGB565

display.draw_text(x, y, text, text_color, bg_color)
```  

### **3. Image Conversion (`image_conversion.py`)**  
This script converts an image to **RGB565 binary format** for display on the screen.  

```python
from PIL import Image

def convert_image_to_rgb565(input_image, output_bin):
    # Open the image
    img = Image.open(input_image)
    img = img.convert("RGB")

    # Resize the image to match the display resolution (optional)
    img = img.resize((480, 320))  # Adjust to your display resolution

    # Convert to RGB565 and write to .bin file
    with open(output_bin, "wb") as f:
        for y in range(img.height):
            for x in range(img.width):
                r, g, b = img.getpixel((x, y))
                # Convert RGB888 to RGB565
                rgb565 = ((r & 0xF8) << 8) | ((g & 0xFC) << 3) | (b >> 3)
                f.write(rgb565.to_bytes(2, "big"))

# Example usage
input_image = "image.png"  # Path to your input image
output_bin = "image.bin"  # Output file
convert_image_to_rgb565(input_image, output_bin)
print(f"Image converted to {output_bin}")
```

P.S. to use the conversion script you need to install PIL

### **4. Image Test (`image_test.py`)**  
This script loads and displays an image from a previously converted `.bin` file.  

```python
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
```  

## **How to Use This Library**  

1. **Install MicroPython** on your microcontroller.  
2. **Upload the `st7796s.py` driver** and any example scripts you need.  
3. **Run the example scripts** to test colors, text, or images.  

Feel free to modify and expand the library for your own projects!  
