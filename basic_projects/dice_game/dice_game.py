#import random
import secrets

def main():
  # Prompt the user to input their roll
  player_roll = int(input("What is the result of your roll with the dice? "))

  # Validate the user's roll
  if player_roll < 1 or player_roll > 6:
    print("Invalid roll. Please enter a number between 1 and 6.")
    return
  
  # Generate a random roll for the player
  # Use secrets.choice() to ensure a fair roll for the player
  # player_roll = random.randint(1, 6)
  # player_roll = secrets.choice(range(1, 7))

  # Generate a random roll for the computer
  # Use secrets.choice() to ensure a fair roll for the computer
  #computer_roll = random.randint(1, 6)
  computer_roll = secrets.choice(range(1, 7))

  # Display the results of the rolls
  print("Player rolled:", player_roll)
  print("Computer rolled:", computer_roll)

  # Determine the winner based on the rolls
  if player_roll > computer_roll:
      print("You won!")
  elif player_roll < computer_roll:
      print("Computer won!")
  else:
      print("It's a tie!")

if __name__ == "__main__":
  main()