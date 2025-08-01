import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no score to show.It's time to play!")
    else:
        print("The current High Score is:{} attempts".format(min(attempts_list)))
def start_game():
    random_number = random.randint(1, 100)
    print(" Hey there! Welcome to the Guessing Game!")
    player_name = input("What is your name? ")
    wanna_play = input("Would you like to play,? (Enter yes/no) ".format(player_name))
    attempts = 0
    show_score()
    while wanna_play.lower() == "yes":
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if int(guess) < 1 or int(guess) > 100:
                raise ValueError("The number must be between 1 and 100.")
            if int(guess) == random_number:
                attempts += 1
                print("Congratulations, {}! You guessed the number in {} attempts.".format(player_name, attempts))
                attempts_list.append(attempts)
                show_score()
                wanna_play = input("Would you like to play again? (Enter yes/no) ")
                if wanna_play.lower() == "no":
                    print("Thank you for playing, {}! Goodbye!".format(player_name))
                    break
            elif int(guess) < random_number:
                print("It's Lower!")
                attempts += 1
            elif int(guess) > random_number:
                print("It's Higher!")
                attempts += 1

        except ValueError as err:
            print("Oops! That is not a valid number. Please try again.")
            print("({})".format(err))
    else:
        print("That's okay, {}! Have a great day!".format(player_name))

if __name__ == "__main__":
    start_game()