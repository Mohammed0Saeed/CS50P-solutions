def main():
  # start an infinite loop
    itemList = {}
    while True:
        #prompt the user to enter an item
        try:
            item = input().lower()
        except EOFError: 
            sortedList = sortDict(itemList)
            for object in sortedList:
                print(str(sortedList[object]), object.upper())
            break
        else:
            #check if the item is in list, and if the item is only on object
            if item not in itemList:
                itemList.setdefault(item)
                itemList[item] = 1
            #if the object is in the list, add 1 to its value
            elif item in itemList:
                itemList[item] += 1

def sortDict(dictionary):
  sortedList = sorted(dictionary)

  sortedDict = {}

  for item in sortedList:
    sortedDict.setdefault(item)
    sortedDict[item] = dictionary[item]

  return sortedDict

main()