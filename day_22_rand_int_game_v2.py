import random

print("Totally Random One-Million-to-One")

running = True
computer = 0
player = 0
counter = 0
computer = random.randint(1,1000000)

while running:
  
  player = int(input("Guess you number!: "))
  print(computer)
  
  if player == computer:
    counter += 1
    print(f"Congratulations! You have guess {counter} time/s.")
  elif player > computer:
    counter += 1
    print("Your guess is too high.")
  elif player < computer:
    counter += 1
    print("Your guess is too low.")
  else:
    break

  if input("Do you want to play again? (y/n): ") == "n":
    running = False
    print("Thanks for playing.")