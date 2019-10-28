#ask the user to input the amount of cables to be removed
print("how many cables should i remove?")
cable_number = int(input())

#create the cable count variable
cable_count = 0
#create the while loop. the loop will repeat and print "cable removed" until the count variable matches the cable number variable inputed by the user.
while (cable_count < cable_number):
    print("cable removed")
    cable_count = cable_count + 1
print("all cables are removed now")