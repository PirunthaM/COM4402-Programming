from idlelib.sidebar import EndLineDelegator

score = int(input("Input score please"))

if score >= 40:
    if score >= 70:
        print("Pass with merit")
    else:
        print("Pass")
else:
    print("Fail")


