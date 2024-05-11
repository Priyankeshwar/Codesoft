# Rock Paper Scissor Game:

import random

choice = ['rock', 'paper', 'scissor']


def user():
    user_choice = input("Choose (rock, paper, scissor): ").lower()
    if user_choice in choice:
        return (user_choice)
    else:
        print("Invalid Choice")


def computer():
    return random.choice(choice)


def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Its a Tie"
    elif user_choice == "rock" and computer_choice == "scissor" or \
            user_choice == "paper" and computer_choice == "rock" or\
            user_choice == "scissor" and computer_choice == "paper":
        return "You Won !!"
    else:
        return "You Lose"


def main():
    user_score = 0
    computer_score = 0

    while True:
        print("\nNew Round:")
        user_choice = user()
        computer_choice = computer()
        print("Your choice:", user_choice)
        print("Computer's choice:", computer_choice)

        result = winner(user_choice, computer_choice)
        print(result)

        if result == "You Won !!":
            user_score += 1

        elif result == "You Lose":
            computer_score += 1

        print(f"Your score: {user_score}, Computer's score: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
