print("Welcome to the tip calculator")
total_bill = input("What was the total bill? $")
a = float(total_bill)

tip = input("What percentage tip would you like to give? [10, 12 or 15]? ")
b = float(tip)

split = input("How many people to split the bill? ")
c = int(split)

split_bill = round((a + (b / 100) * a) / c, 2)

print(f"Each person should pay : {split_bill} dollar")
