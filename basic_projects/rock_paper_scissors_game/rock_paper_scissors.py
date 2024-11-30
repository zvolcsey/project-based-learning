import secrets

def main():
  # Define a list of possible choices
  possible_choices = ['rock', 'paper', 'scissors']

  # Prompt a valid choice from the player
  while True:
    player_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
    if (player_choice in possible_choices):
      break
    else:
      print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

  # Generate a fair choice for the computer
  computer_choice = secrets.choice(possible_choices)

  # Display the results of the choices
  print("Player chose:", player_choice)
  print("Computer chose:", computer_choice)

  # Determine the winner based on the choices and display the result
  if player_choice == computer_choice:
    print("It's a tie!")
  elif (
    (player_choice == 'rock' and computer_choice == 'scissors') or 
    (player_choice == 'paper' and computer_choice == 'rock') or 
    (player_choice == 'scissors' and computer_choice == 'paper')
  ):
    print("You win!")
  else:
    print("Computer wins!")

if __name__ == "__main__":
  main()