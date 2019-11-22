def bridge_crossing(number_of_steps):
    for step in range(number_of_steps):
        print("crossed step: ")
    
    if (number_of_steps>5):
        print("the bridge is collapsing")
    else:
        print("we should keep going")

bridge_crossing(3)
bridge_crossing(7)