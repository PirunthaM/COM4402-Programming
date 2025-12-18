coursework = int(input("Enter coursework mark "))
exam = int(input("Enter exam mark "))

average = (coursework + exam) / 2

match (coursework, exam):
    case (coursework, exam) if coursework < 35 or exam < 35:
        print("Automatic fail")
    case (coursework, exam) if average >= 40:
        print("Module passed")
    case (coursework, exam):
        print("Module failed")