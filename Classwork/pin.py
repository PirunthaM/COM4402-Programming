pin = int(input("Enter pin "))
if pin == 1234:
    colour = input("What is  your favourite colour ")
    if colour.lower() == "blue":
        print("Access granted ")
    else:
        print("Security answer incorrect")
else:
    print("Wrong PIN ")
