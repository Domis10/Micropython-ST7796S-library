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
