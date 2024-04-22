def main():
    # prompt the user to enter a noun
    name = input("Input: ")

    # print a name without vowel letters
    print(remove_vowels(name))

def remove_vowels(name):
    for ltr in name:
        # if the letter is vowel, remove it
        if ltr in ["a", "e", "i", "o", "u"]:
            name = name.replace(ltr, "")
    return name

main()