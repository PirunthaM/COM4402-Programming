number = int(input("Please enter a number "))

match number:
    case number if number % 5 == 0 and number % 3 == 0:
        print("FizzBuzz")
    case number if number % 3 == 0:
        print("Fizz")
    case number if number % 5 == 0:
        print("Buzz")
    case number:
        print("No match")