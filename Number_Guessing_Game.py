import random

# Taking Inputs for lower and upper bounds
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))

# Generating a random number between the lower and upper bounds
num1 = random.randint(lower, upper)
num2 = 0

print("GUESS THE NUMBER")
print("You have 5 chances to guess the true number")

c = 1

while c <= 5:
    num2 = input("Enter a number: ")

    if int(num2) < num1:
        print("Increase the value")
    elif int(num2) > num1:
        print("Decrease the value")
    elif int(num2) == num1:
        print("Congratulations, you won!")
        break

    if c < 5:
        print("You have", 5 - c, "chances left")
    else:
        print("Game over")
        print("The True Number is:", num1)

    c += 1
