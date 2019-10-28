#the following program will decide if beep should lift an object or leave it alone, depending on weight and size of object
#ask what the name of object is
print("what object would you like me to move human?")
user_object = str(input())

#ask weight of object
print("Right, sounds good,\nI will need to check a couple of things first though... safety measures, I'm sure you understand.")
print("\nWhat is the weight of the" ,user_object, "in kg?")
object_weight = float(input())


if ((object_weight >= 10) and (object_weight <15)):
    print("That is almost as heavy as me!")

elif (object_weight >=15):
    print("That is heavier than me!?")

#ask size of object
print("now what about the size of the object? (in cm squared)")
object_size = float(input())
#if the object is both less than 150 cm and less than 15kg then bot will be able to move the object
if ((object_size <=150) and (object_weight <15)):
        print("no problem boss\nMoving object......")
#if not then the program will tell the user it cannot move the item
elif ((object_size>150) or (object_weight>=15)):
    print("I can't move the",user_object )
#and will explain why here depending on the values entered.
    if ((object_size>150) and (object_weight>=15)):
        print("The" ,user_object, "is both too heavy and too big!")
    elif ((object_size<150) and (object_weight>=15)):
        print("I can handle the size but the the",user_object, "is too heavy!")
    elif ((object_size>150) and (object_weight<=15)):
        print("It is light enough however the size of the",user_object, "is too big!")
    
