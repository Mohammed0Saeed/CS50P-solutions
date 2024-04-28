def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # check if the plate have at least two characters and 6 maximum
    if not (2 <= len(s) <= 6):
        return False
    # check if there are characters other than letters and numbers
    for ltr in s:
        if str(0) <= ltr <= str(9) or 65 <= ord(ltr) <= 90 or 97 <= ord(ltr) <= 122:
            continue
        else:
            return False
    # check if the first two characters are letters
    for i in range(2):
        if 65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122:
            continue
        else:
            return False
    # check if the numbers does not start with 0
    index_num = 0
    for ltr in s:
        if str(0) <= ltr <= str(9):
            if ltr == str(0):
                return False
            else:
                break
        else:
            index_num += 1
    # check if letters and numbers are blocks
    while index_num < len(s):
        if str(0) <= s[index_num] <= str(9):
            index_num += 1
        else:
            return False
    return True



if __name__ == "__main__":
    main()
