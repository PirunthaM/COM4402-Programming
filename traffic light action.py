colour = input("Please choose a colour: red, amber, green ")

if colour.lower() == "red":
    print("Stop")
elif colour.lower() == "amber":
    print("Get ready")
elif colour.lower() == "green":
    print("Go")
else:
    print("Invalid colour")