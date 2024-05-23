import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    watch = re.search(r"^<iframe .*src=\"https?://(?:www.)?youtube.com/embed/(\w+)\".*></iframe>$", s)
    if watch:
        return f"https://youtu.be/{watch.group(1)}"
    else:
        return "None"


#<iframe width="560" src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>


if __name__ == "__main__":
    main()

#<iframe src="https://www.youtube.com/embed/tryitOut"></iframe>
