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

for i in range(len(questions)):
    print(questions[i])
    for option in options[i]:
        print(option)

guess = input("Please choose your answer between 1-4...")
