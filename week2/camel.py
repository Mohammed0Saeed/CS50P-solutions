# prompt the user to enter a name with camel case
def main():
  name = input("camelCase: ")
  name = camel_to_snake(name)
  print(name)

# camel_to_snake funcation converts the camel case to snake case
def camel_to_snake(name):
  # identify the capital letter, and then split it into two string
  slicer = 0
  for letter in name:
    if letter.isupper():
      name = name.replace(letter, "_" + letter.lower())
  # return a string with a sep(_)
  return name
      

if __name__ == '__main__':
  main()