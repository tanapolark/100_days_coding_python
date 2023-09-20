import random

print("Epic rock paper scissors battle")

options = ("rock", "paper", "scissors")
running = True

while running:

  player = None
  computer = random.choice(options)

  while player not in options:
    player = input("player please choose (rock, paper, scissors): ").lower()
  
  
  if player == computer:
    print("It's Tie!")
  elif player == "rock" and computer == "scissors":
    print(f"player use {player} to smash computer's {computer}!")
  elif player == "scissors" and computer == "paper":
    print(f"player use {player} to cut computer's {computer}!")
  elif player == "paper" and computer == "rock":
    print(f"player use {player} to defeat computer's {computer}!")
  else:
    print("You lose!")

  if not input("play again?: ").lower() == "y":
    running = False

print("Thanks for playing!")