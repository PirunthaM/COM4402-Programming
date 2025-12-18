days_late = int(input("Please enter number of days late"))
if days_late == 0:
    print("no fine")
elif days_late >= 1 and days_late < 6:
    print("fine = £1")
elif days_late >= 6 and days_late <= 10:
    print("fine = £5")
elif days_late > 10:
    print("fine = £10 and membership review")


