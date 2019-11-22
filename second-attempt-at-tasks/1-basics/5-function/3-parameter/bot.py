def escape_by(action):
    if (action == "jumping over"):
        print("can't do that its too tall!")
    elif(action == "running around"):
        print("but its too wide!")
    elif(action == "going deeper"):
        print("that might just work, lets go deeper!")
    else:
        print("i dont understand that plan")
escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")
escape_by("walking")