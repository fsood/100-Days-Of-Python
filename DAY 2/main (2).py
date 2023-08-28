# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
x = float(height) ** 2
y = int(weight)

bmi = round( y  / x ,2)
print(bmi)

