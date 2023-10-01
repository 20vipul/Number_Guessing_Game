import random

# Generat Random Number


def generate_code():
    """
    Generate a 3 digit list for code
    """
    RnList = [str(num) for num in range(0, 10)]
    random.shuffle(RnList)
    return RnList[:3]

# take input from the Player


def take_guess():
    """
    Ask's user to guess the input
    """
    return list(input("What is your guess : "))


# Generate clues


def generate_clues(code, userGuess):
    """
    takes in both user's guess and code,further compare them to produce final result or to give a clue to solve the code 
    clues are :
        Close: You've guessed a correct number but in the wrong position
        Match: You've guessed a correct number in the correct position
        Nope: You haven't guess any of the numbers correctly
    """
    if userGuess == code:
        return "CODE CRACKED"

    clues = []

    # Compare guess to code
    for i in range(len(userGuess)):
        if userGuess[i] == code[i]:
            clues.append("Match")
        elif userGuess[i] in code:
            clues.append("Close")
    if clues == []:
        return "Nope"
    return clues


# Run Game
print("Welcome to the game \"Crack Code!!\". Lets start ")
secret_code = generate_code()
print("Secret code has been generated. Please enter 3 digit number")
# print(secret_code)

# empty clue report to start with
clue_report = []
while clue_report != "CODE CRACKED":
    # ask for guess
    guess = take_guess()
    # print(guess)
    # print clues
    clue_report = generate_clues(secret_code, guess)
    for clues in clue_report:
        print(clues)
