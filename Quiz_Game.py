import random as rand

### Question Section

def ask_question(question, options, correct_option):
    print("\n" + question)
    for option in options:
        print(option)
    
    answer = input("Enter your Answer (i.e A/B/C/D): ").upper()

    if answer == correct_option:
        print("Correct")
        return 100
    elif answer in ["A", "B", "C", "D"]:
        print("Incorrect")
        return 0
    else:
        print("\nInvalid Input")
        print("You have entered an Invalid Option")
        return ask_question(question, options, correct_option)


def que1():
    return ask_question(
        "Which of the following is the correct way to declare a variable in Python?",
        ["A: x = 10", "B: int x = 10;", "C: var x = 10;", "D: declare x = 10;"],
        "A"
    )

def que2():
    return ask_question(
        "Which of the following is a loop structure in Python?",
        ["A: if", "B: while", "C: def", "D: print"],
        "B"
    )

def que3():
    return ask_question(
        "Which of the following is used to define a function in Python?",
        ["A: function", "B: void", "C: def", "D: define"],
        "C"
    )

def que4():
    return ask_question(
        "What is the purpose of the return statement in a function?",
        ["A: It ends the program.", "B: It exits the loop", "C: It continues the loop", "D: It outputs a value from a function"],
        "D"
    )

def que5():
    return ask_question(
        "Which of the following is the correct way to start a comment in Python?",
        ["A: // This is a comment", "B: # This is a comment", "C: /* This is a comment */", "D: <!-- This is a comment -->"],
        "B"
    )

### Question Generator

def que_generator(id):
    if id == 1:
        return que1()
    elif id == 2:
        return que2()
    elif id == 3:
        return que3()
    elif id == 4:
        return que4()
    elif id == 5:
        return que5()

### Quiz Section

def quiz_game():
    score = 0
    asked_questions = []

    for i in range(2):  # Asking two questions
        que_id = rand.randint(1, 5)
        
        while que_id in asked_questions:
            que_id = rand.randint(1, 5)
        
        asked_questions.append(que_id)
        score += que_generator(que_id)

        if score == 0:
            print("\nGame Over ReStarting.........................")
            return quiz_game()

    return score

### Main Section

total_score = quiz_game()
print("\nYour Score Breakdown")
print(f"Final Score: {total_score}")
