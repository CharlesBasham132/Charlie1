
print("enter first number")
first_number = int(input())

print("enter second number")
second_number = int(input())

print("enter third number")
third_number = int(input())

even_number_counter =0
odd_number_counter =0

if (first_number %2 ==0):
    even_number_counter = even_number_counter + 1
else:
    odd_number_counter = odd_number_counter + 1

if (second_number %2 ==0):
    even_number_counter = even_number_counter + 1
else:
    odd_number_counter = odd_number_counter + 1

if (third_number %2 ==0):
    even_number_counter = even_number_counter + 1
else:
    odd_number_counter = odd_number_counter + 1

print("There are",even_number_counter, "even numbers and",odd_number_counter, "odd numbers")