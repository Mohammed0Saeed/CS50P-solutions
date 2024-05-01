import sys

def main():
    # check if the given argument goes well with the program
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments!")
    elif len(sys.argv) <= 1:
        sys.exit("Too few command-line arguments!")
    elif sys.argv[1].endswith(".py") == False:
        sys.exit("Not a python file!")

  # check if the file exists
    try:
        pyFile = open(sys.argv[1])
    except:
        sys.exit("File doesn't exist!")

    counter = 0

    for line in pyFile:
        # check if the line contains ONLY whitespace or '#'
        if isWhiteSpace(line) == True:
            counter = counter
        else:
            counter += 1

    print(counter)

# check if there is a space

def isWhiteSpace(line):
    for ltr in line:
        if ltr not in [' ', '#', '\t', '\n', '\r', '\v', '\f']:
            return False
        elif ltr == "#":
            return True
    return True

if __name__ == "__main__":
    main()
