score = 0
total_questions = 5

questions = [
    "What is 5 + 3?",
    "What is 12 - 4?",
    "What is 7 x 6?",
    "What is 25 % 5?",
    "What is 9 + 10?",
]

options = [
    ["1) 6", "2) 15", "3) 8", "4) 10"],
    ["1) 8", "2) 6", "3) 7", "4) 5"],
    ["1) 42", "2) 36", "3) 48", "4) 56"],
    ["1) 5", "2) 4", "3) 6", "4) 8"],
    ["1) 18", "2) 19", "3) 20", "4) 21"]
]

answers = [3, 1, 1, 1, 2]

print("Hello, the quiz will now begin...")

for question in range(len(questions)):
    print(questions[question])
    for option in options[question]:
        print(option)

    guess = int(input("Please choose your answer between 1-4..."))

    while guess < 1 or guess > 4:
        print("invalid")
        guess = int(input("Please choose your answer between 1-4..."))

    if guess == answers[question]:
        print("Correct!")
        score = score + 1

    else:
        print("Incorrect")

print("Thank you! Quiz complete...")
print("Your final score is ", score, "out of 5")
percentage = ((score / total_questions) * 100)
print("Your percentage is ", percentage, "%")

