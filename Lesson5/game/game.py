import random


def main():
    level = prompt_user("Level: ")
    result = random.randint(1, level)
    guess = -1
    while guess != result:
        guess = prompt_user("Guess: ")
        check_guess(guess, result)


# Prompt till user enters an integer
def prompt_user(prompt):
    while True:
        try:
            level = int(input(prompt))
            if level <= 0:
                continue
            return level
        except ValueError:
            continue


# Check if the guess is correct
def check_guess(guess, result):
    if guess == result:
        print("Just right!")
    elif guess < result:
        print("Too small!")
    else:
        print("Too large!")


if __name__ == "__main__":
    main()
