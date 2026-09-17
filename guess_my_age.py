import random


def guess_my_age():
    secret_age = random.randint(1, 100)
    max_attempts = 5

    print("Welcome to Guess My Age!")
    print("I'm thinking of an age between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"\nAttempt {attempt}/{max_attempts} - Enter your guess: "))

            if not 1 <= guess <= 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess < secret_age:
                print("Too low!")
            elif guess > secret_age:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed my age in {attempt} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    else:
        print("\nGame over!")
        print(f"My age was {secret_age}.")


if __name__ == "__main__":
    guess_my_age()