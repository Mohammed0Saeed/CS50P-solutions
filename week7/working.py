import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    time = re.search(r"([0-9]?[0-9])(:[0-9][0-9])? (PM|AM) to ([0-9]?[0-9])(:[0-9][0-9])? (PM|AM)", s)

    if time:
        if int(time.group(1)) > 12:
            raise ValueError

        if time.group(3) == "PM":
            if time.group(1) == "12":
                first_time = int(time.group(1))
            else:
                first_time = int(time.group(1)) + 12
        else:
            if time.group(1) == "12":
                first_time = 0
            else:
                first_time = int(time.group(1))

        if int(time.group(4)) > 12:
            raise ValueError

        if time.group(6) == "PM":
            if time.group(4) == "12":
                second_time = int(time.group(4))
            else:
                second_time = int(time.group(4)) + 12
        else:
            if time.group(4) == "12":
                second_time = 0
            else:
                second_time = int(time.group(4))

        if time.group(2) != None:
            first_time_minutes = int(time.group(2).replace(":", ""))
            if int(time.group(2).replace(":", "")) > 59:
                raise ValueError
        else:
            first_time_minutes = 0
        if time.group(5) != None:
            if int(time.group(5).replace(":", "")) > 59:
                raise ValueError
            second_time_minutes = int(time.group(5).replace(":", ""))
        else:
            second_time_minutes = 0

        return f"{first_time:02d}:{first_time_minutes:02d} to {second_time:02d}:{second_time_minutes:02d}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()
