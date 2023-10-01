import random

print("Infinity Dice")

def infinityDice():
  running = True
  while running:
    sides = int(input("How many sides do you want?: "))
    roll = random.randint(1,sides)
    print(f"You rolled {roll}")

    if input("Do you want to roll again? (y/n):") == "n":
      exit()

infinityDice()