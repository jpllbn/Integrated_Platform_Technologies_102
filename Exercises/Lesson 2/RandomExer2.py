import random

def Questions():
    questions = [
        ("Who developed Python?", "Guido  van Rossum"),
        ("What year was the first released of Python?", "1991"),
        ("Where do Python's name derived from?", "Monty Python's Flying Circus"),
        ("Serve as the container that holds temporary value?", "Variable"),
        ("Which animal represents the Python logo?", "Snake")
    ]

    with open('questions.txt', 'w') as AppendFile:
        for i in questions:
            question = list(questions)
            AppendFile.writelines(f"{i}\n")

def main():
    while True:
        try:
            print("QUESTIONS:")
        except:
            pass

Questions()


