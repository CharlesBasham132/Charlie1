
print("how many cables should i avoid?")
user_cable = int(input())
cable_count = 0

while (cable_count < user_cable):
    print("avoiding cable...", end="")
    cable_count = cable_count +1
    print("done",cable_count, "cables avoided")
print("all cables avoided")