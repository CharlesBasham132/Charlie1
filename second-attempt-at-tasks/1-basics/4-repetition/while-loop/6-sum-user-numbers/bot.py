#ask the user how many times the loop should run
print("how many numbers should I sum up?")
#create a total variable, it is important this is created outside and before the while loop
total =0
#the user_number variable will act as the amount of times the loop will run and so the amount..
#..numbers that will be added together
user_number = int(input())
#a count variable is needed so that the program knows when to stop looping,
number_count = 0
while (user_number > number_count):
    #Asks the user to enter a number.
    print("please enter number",number_count+1,"of",user_number)
    #count+1 as to avoid infinite loop
    number_count = number_count+1
    #the temp variable will act as a tempory store of the value of the inputed variable for this occasion of the loop.
    temp = int(input())
    #the temp value is added to the total value
    total = total +temp
    #i added this if statement to display a running total, it will not display before the final sum is revealed
    if (user_number >number_count): 
        print("the running total is:",total)


#prints the total value to the user
print("the sum of the numbers is ",total)

    

    


    


