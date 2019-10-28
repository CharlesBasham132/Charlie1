

print("where should I look for my battery?")
room = str(input())

if (room == "bedroom"):
    print("where in the bedroom should I look?")
    bedroom_location = str(input())
    
    if (bedroom_location == "under the bed"):
        print("Found some shoes but no battery")
    else:
        print("Found mess but no battery")

elif (room == "bathroom"):
    print("where in the bathroom should I look?")
    bathroom_location = str(input())

    if (bathroom_location == "in the bathtub"):
        print("found a rubber duck but no battery")
    else:
        print("found a wet surface but no battery")

elif (room == "lab"):
    print("where in the lab should I look")
    lab_location = str(input())
    if (lab_location == "on the table"):
        print("Yes! I found my battery!")
    else:
        print("found some tools but no battery")

else: print("I don't know where that is but I will keep looking...")