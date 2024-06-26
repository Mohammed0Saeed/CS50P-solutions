from datetime import date
import re
import sys
import inflect


def main():
    Date = input("Date of Birth: ")
    seasons = minutes_in_words(Date)
    print(seasons)


def get_date(Date):
    is_valid = re.search(r"^([0-9][0-9][0-9][0-9])-([0-9]?[0-9])-([0-9]?[0-9])$", Date)

    if is_valid:
        if 1 <= int(is_valid.group(2)) <= 12 and 1 <= int(is_valid.group(3)) <= 30:
            return date(int(is_valid.group(1)), int(is_valid.group(2)), int(is_valid.group(3)))
        else:
            sys.exit("Invalid date")
    else:
        sys.exit("Invalid date")

def minutes_in_words(Date):
    p = inflect.engine()
    birth_date = get_date(Date)
    today = date.today()
    timedelta = abs(today - birth_date)
    minutes = timedelta.days * 24 * 60
    return ",".join(p.number_to_words(minutes, wantlist = True)).replace(",", ", ").replace(" and", "").capitalize() + " minutes"


if __name__ == "__main__":
    main()