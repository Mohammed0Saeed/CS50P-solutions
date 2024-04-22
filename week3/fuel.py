def main():
    # using get_fraction() get a fraction from the user
    x = get_fraction("Fraction: ")

    # print according to the value of x
    if 0.9 <= x <= 1:
        print("F")
    elif 0 <= x <= 0.1:
            print("E")
    else:
        print(str(round(x * 100)) + "%")

def get_fraction(message):
    # repeat the inquery untill the user enters the correct value
    while True:
        fraction = input(message).split("/")
        try:
            x = int(fraction[0])
            y = int(fraction[1])
            value = x / y
        except:
            pass
        else:
            # to make sure that value is in range of [0, 1]
            if 0 <= value <= 1:
                return value

main()
