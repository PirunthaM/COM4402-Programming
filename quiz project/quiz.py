quiz = [
    {"question": "What is 5 + 3?", "options": ["1) 6", "2) 15", "3) 8", "4) 12", "5)quit"], "answer": 3},
    {"question": "What is 12 - 4?", "options": ["1) 8", "2) 6", "3) 7", "4) 5", "5)quit"], "answer": 1},
    {"question": "What is 7 x 6?", "options": ["1) 42", "2) 36", "3) 48", "4) 56", "5)quit"], "answer": 1},
    {"question": "What is 25 % 5?", "options": ["1) 5", "2) 4", "3) 6", "4) 0", "5)quit"], "answer": 4},
    {"question": "What is 9 + 10?", "options": ["1) 18", "2) 19", "3) 20", "4) 21", "5)quit"], "answer": 2}
]

score = 0
total_questions = len(quiz)

print("Hello, the quiz will now begin...")

def get_valid_input(i):
    global quiz
    guess = None
    valid = False
    max_options = len(quiz[i]["options"]) -1

    while valid is not True:
        print(f"Please enter your input between 1-{max_options} or 5 to quit:")
        try:
            guess = int(input())

            if guess == 5:
                return "quit"

            if not 1 <= guess <= max_options:
                print("Value not in range of 1 to 4. ")
            else:
                valid = True
        except:
            print("Input invalid. Try again")

    return guess

def check_guess(i):
    global score

    guess = get_valid_input(i)

    if guess == quiz[i]["answer"]:
        print("Correct!")
        score = score + 1

    if guess == "quit":
        print("You have chosen to quit.")
        exit()

    else:
        print("Incorrect")


def run_quiz():
    for i in range(len(quiz)):
        print(quiz[i]["question"])
        for j in quiz[i]["options"]:
            print(j)
        check_guess(i)

run_quiz()

print("Thank you! Quiz complete...")
print("Your final score is ", score, "out of 5")
percentage = ((score / total_questions) * 100)
print("Your percentage is ", percentage, "%")

