# This script takes a txt file and encodes it with little colored dots.
# See the example: alice_in_wonderland.png
#
# That is the entire text of "Alice's Adventures in Wonderland" encoded
# by dots whose colors are derived from "colors.py"


from PIL import Image, ImageDraw
from colors import colors
import random, sys
import re

f = open(sys.argv[1])
chars = list(f.read())

# These figures generate a 22"x26" image
# with 1/16"
# DPI = 320
s = 20 # Bounding Box Size
p = 4 # Padding
width = 48
height = 48

image = Image.new('RGB', (s * width, s * height), color = 'white')
canvas = ImageDraw.Draw(image)

mySet = {'.', ';', ',', '!', '?'}

for row in range(height):
  for col in range(width):
    # key = random.choice(list(colors.keys()))


    # Attempt to get a character from the character list
    # fallback to whitespace if we run out of characters
    try:
      char = chars[row * width + col].lower()
      key = char if char in colors.keys() else 'other' 
    except IndexError:
      key = ' '

    if char not in mySet: continue



    # Calculate bounding box for dot
    p1 = (s * col + p, s * row + p)
    p2 = (s * (col + 1) - p, s * (row + 1) - p)
    canvas.ellipse([p1, p2], fill = colors[key])

image.save('output/stops.png')
f.close()