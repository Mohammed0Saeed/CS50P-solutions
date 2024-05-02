import sys
from tabulate import tabulate
import csv

# check if the given argument goes well with the program
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments!")
elif len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments!")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a csv file!")

try:
    csvFile = open(sys.argv[1])
except:
    sys.exit("File doesn't exist!")

reader = csv.DictReader(csvFile)

manu = []
i = 0

for row in csvFile:
    manu.append(row.rstrip("\n").split(","))

print(tabulate(manu[1:], manu[0], tablefmt="grid"))