import sys
import PIL
from PIL import Image


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
input = sys.argv[1]
output = sys.argv[2]
if input[-4:].lower() != ".jpg" and input[-4:].lower() != ".png" and input[-5:].lower() != ".jpeg":
    sys.exit("Invalid Input")
elif output[-4:].lower() != ".jpg" and output[-4:].lower() != ".png" and output[-5:].lower() != ".jpeg":
    sys.exit("Invalid Input")
elif input[-4:].lower() == ".jpg" or input[-5:].lower() == ".jpeg":
    if output[-4:].lower() == ".png":
        sys.exit("Input and output have different extensions")
elif input[-4:].lower() == ".png":
    if output[-4:].lower() == ".jpg" or output[-5:].lower() == ".jpeg":
        sys.exit("Input and output have different extensions")

try:
    shirt = Image.open('shirt.png')
    shirt_size = shirt.size

    before_pic = Image.open(input)
    cropped_pic = PIL.ImageOps.fit(before_pic, shirt_size, bleed=0.0, centering=(0.5, 0.5))

    cropped_pic.paste(shirt, shirt)
    cropped_pic.save(output)


except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")