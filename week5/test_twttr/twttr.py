import sys
def main():
    print(shorten(input("Enter a word: ")))


def shorten(word):
    for ltr in word:
        # if the letter is vowel, remove it
        if ltr.lower() in ["a", "e", "i", "o", "u"]:
            word = word.replace(ltr, "")
    return word


if __name__ == "__main__":
    main()
