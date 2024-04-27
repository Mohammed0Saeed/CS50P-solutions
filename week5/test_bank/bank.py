# prompt the user to write a greeting
answer = (input("Greeting: ")).lower().lstrip(" ")

# if the greeting starts with "h" but not "hello"
if answer.startswith("hello"):
    print("$0")
# if the greeting is "hello"
elif answer.startswith("h"):
    print("$20")
else:
    print("$100")


