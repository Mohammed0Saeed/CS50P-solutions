import csv
import sys

# check if the given argument goes well with the program
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments!")
elif len(sys.argv) <= 1:
    sys.exit("Too few command-line arguments!")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit(f"{sys.argv[1]} Not a csv file!")
elif sys.argv[2].endswith(".csv") == False:
    sys.exit(f"{sys.argv[2]} Not a csv file!")

try:
    csvFile = open(sys.argv[1])
except:
    sys.exit(f"Couldn't read {sys.argv[1]}")

# start a reader to input all the values of the array
reader = csv.DictReader(csvFile, fieldnames=['name', 'house'])

fileList = []

# add the file to a list
for row in reader:
    fileList.append(row)

with open(sys.argv[2], "w", newline="") as newFile:
    writer = csv.DictWriter(newFile, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for row in fileList[1:]:
        writer.writerow({
            'first': row['name'].split(",")[1].replace(" ", ""),
            'last': row['name'].split(",")[0],
            'house': row['house']
        })
