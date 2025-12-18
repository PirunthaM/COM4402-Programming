score = int(input("Please input a score"))

if score >= 40:
    if score >= 38 and score <= 42:
        print("Borderline pass, consider review")
    else:
        print("Clear Pass")
else:
    print("Fail")