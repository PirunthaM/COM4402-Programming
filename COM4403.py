score = int(input("Input score please"))

if score >= 70:
    grade = "Distinction"

elif score >= 40:
    grade = "Pass"

else:
    grade = "Fail"

print(grade)

