days_late = int(input("Please enter number of days late"))

match days_late:
    case 0:
        print("no fine")
    case days if 1 <= days <= 5:
        print("£1 fine")
    case days if 6 <= days <= 10:
        print("£5 fine")
    case days:
        print("£10 fine and membership review")

