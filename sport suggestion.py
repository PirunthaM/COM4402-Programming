weather = input("sunny, rainy or cold ")
mood = input("active or tired ")

if weather == "sunny" and mood == "active":
    print("Go for a run.")
elif weather == "sunny" and mood == "tired":
    print("Relax in the park")
elif weather == "rainy":
    print("Indoor workout")
elif weather == "cold":
    print("Go to the gym")
else:
    print("no suggestion available")