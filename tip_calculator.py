print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give?\n"))
people = int(input("How many people to split the bill?\n"))
amount = ((bill / 100 * tip) + bill) / people
print(f"The amount to be paid by each person is \n${round(amount, 2)}")
