day = int(input("Enter day number between 1-7: "))

match day:
    case 1:
        print("Monday - Start of work week")
    case 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend - Relax!")
    case day:
        print("invalid")

