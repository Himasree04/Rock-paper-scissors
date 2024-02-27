import random

def play_rock_paper_scissors():
  """
  Plays a round of Rock-Paper-Scissors with the user.
  """
  # User input
  while True:
    user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
    if user_choice in ("rock", "paper", "scissors"):
      break
    else:
      print("Invalid choice. Please choose rock, paper, or scissors.")

  # Computer selection
  computer_choice = random.choice(["rock", "paper", "scissors"])

  # Display choices
  print(f"You chose: {user_choice.capitalize()}")
  print(f"Computer chose: {computer_choice.capitalize()}")

  # Game logic and result
  if user_choice == computer_choice:
    print("It's a tie!")
  elif user_choice == "rock":
    if computer_choice == "scissors":
      print("Rock smashes scissors! You win!")
    else:
      print("Paper covers rock! You lose.")
  elif user_choice == "paper":
    if computer_choice == "rock":
      print("Paper covers rock! You win!")
    else:
      print("Scissors cuts paper! You lose.")
  else:  # user_choice == "scissors"
    if computer_choice == "paper":
      print("Scissors cuts paper! You win!")
    else:
      print("Rock smashes scissors! You lose.")

# Score tracking (optional)
# Implement score tracking using variables and update them based on the winner

# Play again prompt
while True:
  play_again = input("Play again? (yes/no): ").lower()
  if play_again in ("yes", "no"):
    break
  else:
    print("Invalid choice. Please enter yes or no.")

if play_again == "yes":
  play_rock_paper_scissors()
else:
  print("Thanks for playing!")

if __name__ == "__main__":
  play_rock_paper_scissors()
