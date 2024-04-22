# import sys library to take arguments from the user
import sys
from random import randint
# import frank, ian and glens letters for the output
import pyfiglet

# setting the figlet function
figlet = pyfiglet.Figlet()

# list of the fonts
fonts = figlet.getFonts()

# check if the user prompted no prefrence
if len(sys.argv) == 1:
    # without specified font

    message = input("Input: ")
    index = randint(0, (len(fonts) - 1))

    figlet.setFont(font = fonts[index])

    print(figlet.renderText(message))

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--f"] and sys.argv[2] in fonts:
    # with specified font

    message = input("Input: ")
    figlet.setFont(font = sys.argv[2])

    print(figlet.renderText(message))

else:
    sys.exit("Invalid usage")
