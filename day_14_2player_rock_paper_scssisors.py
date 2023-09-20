from getpass import getpass

print("Epic rock paper scissors battle")

options = ("rock", "paper", "scissors")
running = True

while running:

  player1 = None
  player2 = None

  while player1 not in options:
    player1 = getpass("player1 please choose (rock, paper, scissors): ").lower()
  
  while player2 not in options:
    player2 = getpass("player2 please choose (rock, paper, scissors): ").lower()
  
  if player1 == player2:
    print("It's Tie!")
  elif player1 == "r" and player2 == "s":
    print(f"player1 use {player1} to smash player2's {player2}!")
  elif player1 == "s" and player2 == "p":
    print(f"player1 use {player1} to cut player2's {player2}!")
  elif player1 == "p" and player2 == "r":
    print(f"player1 use {player1} to defeat player2's {player2}!")
  elif player2 == "r" and player1 == "s":
    print(f"player2 use {player2} to smash player1's {player1}!")
  elif player2 == "s" and player1 == "p":
    print(f"player2 use {player2} to cut player1's {player1}!")
  else:
    print(f"player2 use {player2} to defeat player1's {player1}!")

  if not input("play again?: ").lower() == "y":
    running = False

print("Thanks for playing!")