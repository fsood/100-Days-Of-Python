# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
first = name1.lower()
second = name2.lower()

both_names = first + " " + second

# counting the no. of times true love appears
t_times = both_names.count('t')
r_times = both_names.count('r')
u_times = both_names.count('u')
e_times = both_names.count('e')
l_times = both_names.count('l')
o_times = both_names.count('o')
v_times = both_names.count('v')

true = t_times + r_times + u_times + e_times
love = l_times + o_times + v_times + e_times

love_score = int(str(true) + str(love))

if 10 > love_score or love_score > 90:
    print(f'"Your score is {love_score},you go together like coke and mentos."')
elif 50 >= love_score >= 40:
    print(f'"Your score is {love_score}, you are alright together."')
else:
    print(f"Your score is {love_score}.")
