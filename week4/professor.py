import random


def main():
    # get a level from the user
    level = get_level()

    # iterate over the 10 questions
    score = 0
    for i in range(10):
        minusScore = 0
        wrongAnswer = 0
        # select a random number for x or y
        x = generate_integer(level)
        y = generate_integer(level)

        # check that the user inputs only integer numbers
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
            except:
                pass
            else:
                # check of the answer is correct
                if answer == (x + y):
                    score = score + 1 + minusScore
                    break
                elif wrongAnswer < 2:
                    print("EEE")
                    wrongAnswer += 1
                    minusScore = -1
                else:
                    print(f"{x} + {y} = {x + y}")
                    break
    print(f"Score: {score}")






def get_level():
    # make sure that the user inputs a positive integer between 1 and 3
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                raise Exception
        except:
            pass
        else:
            return level



def generate_integer(level):
    match level:
        case 1:
            integer = random.randint(0, 9)
        case 2:
            integer = random.randint(10, 99)
        case 3:
            integer = random.randint(100, 999)

    return integer


if __name__ == "__main__":
    main()
