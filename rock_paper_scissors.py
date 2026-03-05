import random

print("---- ROCK PAPER SCISSORS GAME ----")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    print("\nChoose rock, paper, or scissors")
    user_choice = input("Your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Try again.")
        continue

    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("Result: It's a tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("Result: You win!")
        user_score += 1

    else:
        print("Result: Computer wins!")
        computer_score += 1

    print("\nScore")
    print("You:", user_score)
    print("Computer:", computer_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Score")
        print("You:", user_score)
        print("Computer:", computer_score)
        print("Thanks for playing!")
        break