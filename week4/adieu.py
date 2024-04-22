import inflect
import sys

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ")
    except EOFError:
        print(f"\nAdieu, adieu, to {p.join(names[0:])}")
        sys.exit()
    else:
        names.append(name)


