score = 0
current_questions = 0
total_questions = 5

questions = [
    "What is 5 + 3?",
    "What is 12 - 4?",
    "What is 7 x 6?",
    "What is 25 % 5?",
    "What is 9 + 10?",
]

options = [
    ["6", "15", "8", "10"],
    ["8", "6", "7", "5"],
    ["42", "36", "48", "56"],
    ["5", "4", "6", "8"],
    ["18", "19", "20", "21"]
]

correct_answers = [3, 1, 1, 1, 2]

print("Hello, the quiz will now begin...")

while current_questions<total_questions:
    print(questions[current_questions], current_questions + 1)

    current_options = options[current_questions]

    print(current_options)

    guess = int(input("Enter your answer between 1-4..."))

    if guess != "2" and guess != "2" and guess != "3" and guess != "4":
        print("Thank you for your answer")
    else:
        print("That is an incorrect option, please choose between 1-4")

    correct_answer = correct_answers[current_questions]

    if guess == correct_answer:
        score = score + 1
        print("Well done, that is correct")
    else:
        print("incorrect")

    current_question = current_questions + 1

print("Thank you for participating. Your score and percentage will be displayed below...")
print ("Your final score is ", score)

percentage = (score / total_questions) * 100
print("Your final percentage is ", percentage)


