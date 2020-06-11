import random

comp_guess = random.randint(1, 101)

right_guess = 0

while right_guess == 0:
    user_guess = int(input("Make a guess: "))
    if user_guess == comp_guess:
        print("Awesome, you guessed right!")
        right_guess += 1
    else:
        print("Wrong Guess.")
        if comp_guess >= 5 and comp_guess < 94 :
            for x in range(comp_guess - 5, comp_guess + 1):
                if user_guess == x:
                    print("Pretty close above")
            for x in range(comp_guess, comp_guess + 6):
                if user_guess == x:
                    print("Pretty close below")
            for x in range(comp_guess - 15, comp_guess -5):
                if user_guess == x:
                    print("Close above")
            for x in range(comp_guess +6, comp_guess + 16):
                if user_guess == x:
                    print("Close below")
        elif comp_guess >= 94:
            for x in range(90, 101):
                if user_guess == x:
                    print("Pretty close")
        else:
            for x in range(0, 10):
                if user_guess == x:
                    print("Pretty close")