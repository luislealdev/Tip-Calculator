print("Welcome to the tip calculator")
totalBill = float(input("What was the total bill? "))
people = int(input("How many people to split the bill? "))
percentage = int(input("What percentage tip would you like to give? (10, 12 or 15)? "))

totalToPay = totalBill+totalBill*(percentage/100)
totalToPayPerPerson = round(totalToPay/people, 2)

print(f"Total to pay for person: {totalToPayPerPerson}")