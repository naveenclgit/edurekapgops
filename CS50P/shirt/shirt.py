import sys
import os
from PIL import Image, ImageOps


def main():
    callvalidation()

    try:
        muppetin = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    muppet = ImageOps.fit(muppetin, size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])
    print("OK")


def callvalidation():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    iflext = os.path.splitext(sys.argv[1])
    oflext = os.path.splitext(sys.argv[2])

    if iflext[1].lower() not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid input")

    if oflext[1].lower() not in [".jpg", ".jpeg", ".png"]:
        sys.exit("Invalid output")

    if iflext[1].lower() != oflext[1].lower():
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
