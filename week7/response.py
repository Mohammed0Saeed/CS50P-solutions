from validator_collection import checkers

def main():
    print(isValid(input("Enter your email address: ")))

def isValid(s):
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
