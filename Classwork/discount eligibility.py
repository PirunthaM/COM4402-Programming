is_student = (input("yes or no "))
age = int(input("Enter age "))

if is_student == "yes" or age < 18:
    print("Discount applied")
else:
    print("No discount")
