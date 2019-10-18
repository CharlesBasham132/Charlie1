#bmi calculation program
#ask user name and alocate input string
print("what is your name?")
user_name = str(input())
#ask user age and alocate age integer variable
print("hi there" ,user_name, "How old are you? (in years)")
user_age = int(input())
#ask user height and alocate float
print("nice, how tall are you? (in metres")
user_height = float(input())
#ask user weight and alocate float
print("ok, and finally how much do you weigh(in kilograms")
user_weight = float(input())

#bmi calculation,     / is divide and **2 is squared
user_bmi = user_weight / user_height**2


#present user's name, age and bmi
print(user_name, "You are", user_age, "years old and Your bmi is:",user_bmi)