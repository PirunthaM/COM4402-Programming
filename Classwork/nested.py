from idlelib.sidebar import EndLineDelegator
age = int(input("Please enter your age "))

if age < 5:
    print ("Free entry")
elif age > 5 and age < 18:
    print("Child ticket")
elif (age > 17 and age < 65):
    print("Adult ticket")
elif age > 65:
    print("Senior ticket")


