import random

def charStatGen():
  six_sided_roll = random.randint(1,6)
  eight_sided_roll = random.randint(1,8)
  health = six_sided_roll * eight_sided_roll
  return health

name = str(input("Name your character: "))
health = charStatGen()
print(f"Yor character name is {name}. Their health is {health}.")