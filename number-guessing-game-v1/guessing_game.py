"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
MIN_VALUE = 1
MAX_VALUE = 10
LINE_WIDTH = 50
STARTING_HIGH_SCORE = 100

# Iterate until proper value is entered
def process_guess():
    valid = False
    while valid != True:
        guess = input("Enter your guess: ")
        try:
            guess = int(guess)
            if guess < 1:
                raise IndexError(f"Your guess needs to be at least 1")
            elif guess > MAX_VALUE:
                raise IndexError(f"Your guess can't be greater than {MAX_VALUE}")
        # catch out of range errors
        except IndexError as err:
            print(err)
        # catch other value errors
        except ValueError:
            print(f"Please enter an integer between {MIN_VALUE} and {MAX_VALUE}")
        else:
            valid = True

    return guess

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    high_score = STARTING_HIGH_SCORE
    print('*' * LINE_WIDTH)
    print("Welcome to Guess My Number!!!")
    print('*' * LINE_WIDTH)
    print()
    # set toggle for continuing game
    continue_game = True
    while continue_game:
        num_guesses = 1
        if high_score != STARTING_HIGH_SCORE:
            print(f"Current High Score: {high_score}")
        else:
            print("There is currently no high score, so it's all you!!")
        print(f"I'm thinking of a number between 1 and {MAX_VALUE}. Your job is to guess it!")
        num_to_guess = random.randint(MIN_VALUE + 1, MAX_VALUE)
        guess = process_guess()
        while guess != num_to_guess:
            if num_to_guess < guess:
                print("It's lower")
            else:
                print("It's higher")
            
            num_guesses += 1
            guess = process_guess()
        
        # pluralize "try"
        if num_guesses == 1:
            try_text = "try"
        else:
            try_text = "tries"
    
        # Display success message with number of guesses
        print(f"You got it in {num_guesses} {try_text}!")

        # record high score
        if num_guesses < high_score:
            if high_score != STARTING_HIGH_SCORE:
                print(f"You beat the prior best score of {high_score}. Great job!!")

            high_score = num_guesses

        # start another game
        another_game = input("Would you like to play again? y/n: ")
        if another_game.lower() == 'y':
            continue_game = True
            print('*' * LINE_WIDTH)
            print()
        else:
            continue_game = False
            print("Thank you so much for playing!! I hope you enjoyed the game!!")
            print('*' * LINE_WIDTH)



# Kick off the program by calling the start_game function.
start_game()