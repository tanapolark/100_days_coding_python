import time
import os
import random

def six_sided_roll():
  sixsResult = random.randint(1,6)
  return sixsResult

def eight_sided_roll():
  eightsResult = random.randint(1,8)
  return eightsResult

def stat_generator():
  stat = six_sided_roll() * eight_sided_roll()
  return stat

def charactor_build():
  print("====================")
  print("Character Builder")
  name = input("Name you character: ")
  time.sleep(1)
  print("====================")
  race = input("Character Type (Human, Elf, Wiard, Orc): ")
  time.sleep(1)
  print("====================")
  print(f"{name} the {race}")
  health = stat_generator()
  strength = round(stat_generator() / 2) + 12
  print(f"Health: {health}")
  print(f"Strenght: {strength}")
  print("====================")
  time.sleep(1)

running = True

while running:
  charactor_build()

  if not input("Want to generate again? (y/n): ") == "y":
    os.system("clear")
    running = False