grade = input("input grade letter A, B, C, D, F: ")

match grade:
    case "A":
        print("80-100")
    case "B":
        print("70-79")
    case "C":
        print("60-55")
    case "D":
        print("54-45")
    case "F":
        print("44-30")
    case grade: print("Invalid grade")
