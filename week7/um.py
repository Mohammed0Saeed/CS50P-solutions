import re


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    um = re.findall(r"\b(um)\b", s)
    counter = 0
    for word in um:
        if word == "um":
            counter += 1
    return counter


if __name__ == "__main__":
    main()
