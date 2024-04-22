months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    #prompt the user to enter the date
    date = input("Date: ")

    try:
        # if the date matches MM DD, YYYY
        if "," in date and date.replace(",", "").split(" ")[0] in months and 1 <= int(date.replace(",", "").split(" ")[1]) <= 31:
            #reorder the date
            formDate = date.replace(",", "").split(" ")
            print(f"{formDate[2]}-{(months.index(formDate[0]) + 1):02}-{int(formDate[1]):02}", end="")

        # if the date matches MM/DD/YYYY type
        elif 1 <= int(date.replace(" ", "").split("/")[0]) <= 12 and 1 <= int(date.replace(" ", "").split("/")[1]) <= 31:
            #reorder the date
            formDate = date.replace(" ", "").split("/")
            print(f"{formDate[2]}-{int(formDate[0]):02}-{int(formDate[1]):02}", end="")
        else:
          raise Exception()
    except:
        pass

    else:
        #print the date
        break
