#Write your code below this row 👇
sum_of_even = 0
for number in range (0, 101, 2):
  sum_of_even += number
print(sum_of_even)

#or
sum_of_even1 = 0
for numbers in range(1,101):
    if numbers % 2 == 0:
        sum_of_even1 += numbers
print(sum_of_even1)