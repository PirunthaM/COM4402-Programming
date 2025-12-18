colour = input("Please choose a colour: red, amber, green ")

match colour:
    case "red":
        print("Stop")
    case "amber":
        print("Get ready")
    case "green":
        print("Go")
    case colour:
        print("Invalid colour")