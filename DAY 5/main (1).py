student_height = input("Input a list of student heights ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)

# write your code
total_height = 0
for height in student_height:
    total_height += height
# print total height

number = 0
for total_number in student_height:
    number += 1
# print total number of heights

average_height = total_height / number
print(round(average_height))
