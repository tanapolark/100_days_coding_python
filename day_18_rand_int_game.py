import random

counter = 0
print("Guess the number game (1-1000)")
running = True

while running:
  computer = random.randint(1, 1000)
  player = int(input("Guess the correct answer!: "))
  if player < computer:
    counter += 1
    print("Too low!")
  elif player > computer:
    counter += 1
    print("Too high!")
  elif player == computer:
    counter += 1
    print(f"Correct you guess {counter} attempts!")
  else: 
    running = False
    print("Thanks for playing.")

