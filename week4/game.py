from random import randint
import sys

def main():
  # promt the user to enter a positive integer
  while True:
    try:
      level = int(input("Level: "))
    except:
      pass
    else:
      if level >= 1:
        runGame(level)
        break

def runGame(level):
  number = randint(1, level)
  while True:
    try:
      guess = int(input("Guess: "))
    except:
      pass
    else:
      if guess > 0:
        if guess > number:
          print("Too large!")
        elif guess == number:
          print("Just right!")
          sys.exit()
        elif guess < number:
          print("Too small!")

main()
