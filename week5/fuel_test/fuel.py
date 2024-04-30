def main():
    number = input("Enter a number: ")
    percentage = gauge(convert(number))
    print(percentage)



def convert(fraction):
    # check if the user's input is correct
    # check if y is not 0
    if "/0" in fraction and fraction[0] != "0":
        raise ZeroDivisionError

    # devide fraction into two arrays
    fraction = fraction.split("/")

    x = int(fraction[0])
    y = int(fraction[1])
    value = (x / y) * 100
    # to make sure that value is in range of [0, 1]
    if 0 <= value <= 100:
        return int(value)
    else:
        raise ValueError


def gauge(percentage):
    # print according to the value of x
    if 99 <= percentage <= 100:
        return "F"
    elif 0 <= percentage <= 1:
        return "E"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
