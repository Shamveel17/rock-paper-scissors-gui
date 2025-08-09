import random

def play_game():
    options = ["rock", "paper", "scissors"]  

    user = input("Enter your name: ")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Enter Rock, Paper, or Scissors (or 'quit' to stop): ").lower()

        if user_choice == "quit":
            print("\nFinal Scores:")
            print(f"{user}: {user_score}")
            print(f"Computer: {computer_score}")
            print("Thanks for playing! Goodbye 👋")
            break
        
        if user_choice not in options:
            print("Invalid choice! Please try again.")
            continue

        computer = random.choice(options)
        print(f"Computer chose: {computer}")

        if user_choice == computer:
            print("It's a Tie!")
        elif (user_choice == "rock" and computer == "scissors") or \
             (user_choice == "paper" and computer == "rock") or \
             (user_choice == "scissors" and computer == "paper"):
            print(f"{user} Wins this round! 🎉")
            user_score += 1
        else:
            print("Computer Wins this round! 😢")
            computer_score += 1

        
        print(f"Score -> {user}: {user_score} | Computer: {computer_score}\n")

play_game()
