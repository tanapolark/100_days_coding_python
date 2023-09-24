import random

print("Epic rock paper scissors battle")

match = float(input("Please enter number of round you want to play: "))
print(f"You want to play {match} match.")
options = ("rock", "paper", "scissors")
running = True
playerwin = 0
computerwin = 0

while running:

  player = None
  computer = random.choice(options)
  

  while player not in options:
    player = input("player please choose (rock, paper, scissors): ").lower()
    
    print(f"Player choose {player}!")
    print(f"Computer choose {computer}!")
  
  if player == computer:
    print("It's Tie!")
    print(f"Player: {playerwin}")
    print(f"Computer: {computerwin}")
    #continue
  elif player == "rock" and computer == "scissors":
    print(f"player use {player} to smash computer's {computer}!")
    playerwin += 1
    print(f"Player: {playerwin}")
    print(f"Computer: {computerwin}")
    #continue
  elif player == "scissors" and computer == "paper":
    print(f"player use {player} to cut computer's {computer}!")
    playerwin += 1
    print(f"Player: {playerwin}")
    print(f"Computer: {computerwin}")
    #continue
  elif player == "paper" and computer == "rock":
    print(f"player use {player} to defeat computer's {computer}!")
    playerwin += 1
    print(f"Player: {playerwin}")
    print(f"Computer: {computerwin}")
    #continue
  else:
    print("You lose!")
    computerwin += 1
    print(f"Player: {playerwin}")
    print(f"Computer: {computerwin}")
    #continue

  if playerwin >= round(match/2):
    print("You win!")
    break
  elif computerwin >= round(match/2) + 1:
    print("Computer win!")
    break

  #if not input("play again?: ").lower() == "y":
    #running = False

print("Thanks for playing!")
