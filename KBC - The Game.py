# This is a quiz game called KBC
import random
questions = [
    {
        "question": "What is the capital of France?",
        "choices": {"[A]": "Rome", "[B]": "London", "[C]": "Paris", "[D]": "Berlin"},
        "correct": "C"
    },
    {
        "question": "What is the symbol for the element iron?",
        "choices": {"[A]": "Ir", "[B]": "Fe", "[C]": "[A]u", "[D]": "Ag"},
        "correct": "B"
    },
    {
        "question": "What is the highest mountain peak in the world?",
        "choices": {"[A]": "Mount Everest", "[B]": "K2", "[C]": "Makalu", "[D]": "Lhotse"},
        "correct": "A"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "choices": {"[A]": "William Shakespeare", "[B]": "Jane Austen", "[C]": "Mark Twain", "[D]": "J.R.R. Tolkien"},
        "correct": "A"
    },
    {
        "question": "What is the currency of Japan?",
        "choices": {"[A]": "Pound", "[B]": "Dollar", "[C]": "Euro", "[D]": "Yen"},
        "correct": "D"
    },
    {
        "question": "Who was the first president of the United States?",
        "choices": {"[A]": "George Washington", "[B]": "Thomas Jefferson", "[C]": "John Adams", "[D]": "Benjamin Franklin"},
        "correct": "A"
    },
    {
        "question": "Who invented the lightbulb?",
        "choices": {"[A]": "Thomas Edison", "[B]": "Alexander Graham Bell", "[C]": "Albert Einstein", "[D]": "Isaac Newton"},
        "correct": "A"
    },
    {
        "question": "What is the capital of Australia?",
        "choices": {"[A]": "Sydney", "[B]": "Melbourne", "[C]": "Brisbane", "[D]": "Canberra"},
        "correct": "D"
    },
    {
        "question": "What is the symbol for the element oxygen?",
        "choices": {"[A]": " O", "[B]": " H", "[C]": " C", "[D]": " N"},
        "correct": "A"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": {"[A]": "Earth", "[B]": "Jupiter", "[C]": "Saturn", "[D]": "Uranus"},
        "correct": "B"
    },
    {
        "question": "Who painted the famous artwork 'The Starry Night'?",
        "choices": {"[A]": "Pablo Picasso", "[B]": "Claude Monet", "[C]": "Vincent van Gogh", "[D]": "Salvador Dali"},
        "correct": "C"
    },
    {
        "question": "What is the capital of Brazil?",
        "choices": {"[A]": "Rio de Janeiro", "[B]": "Sao Paulo", "[C]": "Brasilia", "[D]": "Belo Horizonte"},
        "correct": "C"
    },
    {
        "question": "What is the largest ocean in the world?",
        "choices": {"[A]": "Pacific Ocean", "[B]": "Atlantic Ocean", "[C]": "Indian Ocean", "[D]": "Arctic Ocean"},
        "correct": "A"
    }
]

# Variables
random.shuffle(questions)  # shuffle questions
tMoney = random.randint(1000, 70000)
pMoney = 0
correct_ans = 0
wrong_ans = 0

print("\n[Welcome to KBC]\n\n Enter your name to start: ", end="")
name = input("")
print("\n", end="")  # enter

for j in range(5):
    question = questions[j]["question"]
    print(question, "\n")

    # Choices
    choices = questions[j]["choices"]
    for k, v in choices.items():
        print(k, v)
    print("\n", end="")  # enter

    # Answer & Correct
    answer = input("Enter your choice: ")
    correct = questions[j]["correct"]

    # Add Money/points
    if answer == correct:
        pMoney += tMoney
        correct_ans += 1
        print("[CORRECT ANSWER]\n")
    elif answer != correct:
        wrong_ans += 1
        print("[WRONG ANSWER]\n")
    else:
        print("[INVALID INPUT]\n")

# Announce
if correct_ans != 0:
    print(f"Congratulations {name}!! you won", pMoney, "Rs")
    print(f"Correct answers: {correct_ans}, Incorrect answers: {wrong_ans}")
else:
    print(f"Better luck next time {name} :)")
    print(f"Correct answers: {correct_ans}, Incorrect answers: {wrong_ans}")
