print("enter a number you want to find the factorial of")
number = int(input())

count =0
total =1

while(count<number):

    count =count+1
    total = total * count

print("the factorial of",number, "is",total)