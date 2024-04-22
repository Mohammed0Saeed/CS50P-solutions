#prompt the user to enter the answer
answer = input("What is the Answer to the Great Question of Life, the universe, and everything? ")

# using match cases check if the answer correct
match answer.lower().replace(" ", ""):
  case "42" | "forty-two" | "fortytwo":
    print("yes")
  case _:
    print("no")