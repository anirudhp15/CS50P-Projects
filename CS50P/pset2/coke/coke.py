amount_due = 50

while amount_due > 0:

    print("Amount Due: " + str(amount_due))
    pay = int(input("Insert Coin: "))

    if pay <= 25:
        if pay < amount_due:
            amount_due -= pay
        elif pay > amount_due:
            change = pay - amount_due
            print("Change Owed: " + str(change))
            amount_due = -1
        elif pay == amount_due:
            print("Change Owed: 0")
            amount_due = -1



