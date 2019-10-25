

print("which direction should i paint? (up, down, left, right)")
user_direction = str(input())

if (user_direction == "up"):
    print("painting upwards")
elif (user_direction == "down"):
    print("painting downwards")
elif (user_direction == "right"):
    print("painting rightwards")
elif (user_direction == "left"):
    print("painting leftwards")
else:
    print("I do not understand that direction")
    