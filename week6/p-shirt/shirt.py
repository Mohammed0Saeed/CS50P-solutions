import sys
from PIL import Image
from PIL import ImageOps

def main():
    # check if the input is correct
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments!")
    elif len(sys.argv) <= 2:
        sys.exit("Too few command-line arguments!")

    img_1 = check_image(sys.argv[1])
    img_2 = check_image(sys.argv[2])

    # check that the files have the same extension
    if img_1.split(".")[1] != img_2.split(".")[1]:
        sys.exit("Input and output have different extensions!")
    else:
        extension = img_2.split(".")[1]
        name = img_2

    # check if the files exist
    try:
        shirt = Image.open("shirt.png")
    except:
        raise FileNotFoundError

    try:
        img_1 = Image.open(check_image(sys.argv[1]))
    except:
        raise FileNotFoundError

    # set the size of each photo to 600x600
    img_1 = ImageOps.fit(img_1, (600, 600))
    shirt = ImageOps.fit(shirt, (600, 600))

    # overlay the first the shirt to the image
    img_1.paste(shirt, shirt)

    #save the image as the given name in the second command-line argument
    img_1.save(img_2)


# a function to check if the image is valid
def check_image(image):
    # check if the image is supported
    if image.endswith(".jpg") or image.endswith(".png") or image.endswith(".jpeg"):
        return image
    else:
        sys.exit("Invalid Input!")

if __name__ == "__main__":
    main()
