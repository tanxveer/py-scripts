import sys
from PIL import Image

# pass image through command line argument
image_path = sys.argv[1]
img = Image.open(image_path)

# resize the image
width, height = img.size
aspect_ratio = height/width
new_width = 100
new_height = aspect_ratio * new_width * 0.50
img = img.resize((new_width, int(new_height)))

# convert image into grayscale format
img = img.convert('L')
pixels = img.getdata()

# replace each pixel with a character from array
chars = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
new_pixels = [chars[pixel//25] for pixel in pixels]
new_pixels = ''.join(new_pixels)

# split string of chars into mutliple strings of length equal to new width and create list
new_pixel_count = len(new_pixels)
ascii_image = [new_pixels[index:index + new_width] for index in range (0, new_pixel_count, new_width)]
ascii_image = "\n".join(ascii_image)
print(ascii_image)

# write these multiple string to text file
with open("ascii_image.txt", "w") as f:
    f.write(ascii_image)