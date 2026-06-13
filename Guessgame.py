import random

print("===== NUMBER GUESSING GAME =====")

secret_number = random.randint(1, 100)
attempts = 0

print("I have selected a number between 1 and 100.")
print("Try to guess it!")

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too Low! Try again.")

        elif guess > secret_number:
            print("Too High! Try again.")

        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

    except ValueError:
        print("Invalid input! Please enter a valid number.")