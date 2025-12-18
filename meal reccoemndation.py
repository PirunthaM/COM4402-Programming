time_of_day = input("morning, afternoon, evening ")
is_hungry = input(" yes or no ")

if is_hungry == "no":
    print("Have some water")
elif is_hungry == "yes":
    if time_of_day == "morning":
        print("Have breakfast")
    elif time_of_day == "aftenoon":
        print("Have lunch")
    elif time_of_day == "evening":
        print("Have dinner")
else:
    print("snack time")