coursework = int(input("Please input coursework mark "))
exam = int(input("Please input exam mark "))
average = (coursework + exam) % 2

if coursework < 35:
    print("Automatic fail (component below 35)")
    else exam < 35:
        print("Automatic fail (component below 35)")
    print("Automatic fail (component below 35)")
elif average >= 40:
    print("Module passed")
else:
    print("Module failed(average below 40)")