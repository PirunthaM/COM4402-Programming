age = int(input("Please enter your age "))

match age:
    case age if age < 5:
        print("Free entry")
    case age if age <= 17:
        print("Child ticket")
    case age if age <= 64:
        print("Adult ticket")
    case age if age > 65:
        print("Senior ticket")