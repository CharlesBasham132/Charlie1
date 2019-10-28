
print("what type of adventure should I have?")
adventure_type = str(input())
if ((adventure_type == "short") or (adventure_type == "scary")):
    print("entering the dark forest...")

elif((adventure_type == "safe") or (adventure_type == "long")):
    print("taking the long way around...")
else:
    print("not sure which route to take")