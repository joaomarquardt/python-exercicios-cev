import random


def guessing_game():
    secret_number = random.randint(1, 100)
    is_game_over = False
    while not is_game_over:
        print("Welcome to the number guessing game.")
        print("I'm thinking of a number between 1 and 100.")
        ans = input('Do you want to see the answer? ')
        if ans == 'y':
            print(f'The answer is {secret_number}')
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
        if difficulty == 'easy':
            num_guesses = 10
        elif difficulty == 'hard':
            num_guesses = 5
        print(f"You have {num_guesses} attempts remaining to guess the number.")
        while num_guesses > 0:
            guess = int(input("Make a guess: "))
            num_guesses -= 1
            if guess > secret_number:
                print("Too high.")
                print("Guess again.")
                print(f"You have {num_guesses} guesses remaining to guess the number.")
            elif guess < secret_number:
                print("Too low.")
                print("Guess again.")
                print(f"You have {num_guesses} guesses remaining to guess the number.")
            else:
                break
        if guess == secret_number:
            print(f"You got it! The number was {secret_number}.")
            if input("Would you like to play again? Type 'y' or 'n': ") == 'y':
                guessing_game()
            else:
                is_game_over = True
        elif num_guesses == 0:
            print(f"You lose. The number was {secret_number}")
            if input("Would you like to play again? Type 'y' or 'n': ") == 'y':
                guessing_game()
            else:
                is_game_over = True


guessing_game()