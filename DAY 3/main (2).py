# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
x = float(height) ** 2
y = int(weight)

bmi = round(y / x)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif 25 > bmi:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 30 > bmi:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 35 > bmi:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
