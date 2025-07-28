# Guessing Game - Beckham , Johnny , Joram

import random

def  generate_random_number():   
    return random.randint(1,100)


#Grabs the users input 

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter a number between 1 and 100: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Please enter a valid integer.")
get_user_guess()
        
# one round of Guessing Game
    
def play_guessing_game():

 
    secret_number = generate_random_number()

    attempts = 0 

#Tells the user if there guess is too low or high from the secret_number 

    while True :

        guess = get_user_guess()
 
        attempts += 1

        if guess == secret_number:
            print(f"Correct! You guessed the secret_number in {attempts} attempts.")
        elif guess > secret_number:
            print("too high try once more")
        else:
            print("too low try once more")

def game_loop():
    while True:
        play_guessing_game()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    game_loop()