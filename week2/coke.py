due = 50
while True:
    print("Amount Due:", due)
    coin = int(input("Insert a coin: "))

    if coin in [5, 10, 25]:
        due = due - coin
        if due >= 0:
            if due != 0:
                continue
            else:
                print("Change Owed:", abs(due))
                break
        else:
            print("Change Owed:", abs(due))
            break
