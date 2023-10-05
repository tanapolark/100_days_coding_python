import os
import time
import random

def health_gen():
  return random.randint(1,6) * random.randint(1,8)
  
def strength_gen():
  return  round(random.randint(1,6) * random.randint(1,8) / 2) + 12

def initiative():
  return random.randint(1,100)

running = True

name_1 = input("Name first character: ")
race_1 = input("Pick first character's race: ")
name_2 = input("Name second character: ")
race_2 = input("Pick second character's race: ")
health_1 = health_gen()
health_2 = health_gen()
strength_1 = strength_gen()
strength_2 = strength_gen()
round = 0
damage = abs(strength_1 - strength_2) + 1

print("=========================")
print(f"First champion is {name_1} the {race_1}!")
print(f"HEALTH: {health_1}")
print(f"STRENGTH: {strength_1}")
print("-------------------------")
print(f"Second champion is {name_2} the {race_2}!")
print(f"HEALTH: {health_2}")
print(f"STRENGTH: {strength_2}")
print("=========================")

while running:
  initiative_1 = initiative()
  initiative_2 = initiative()
  print(f"{name_1} rolled initiative for {initiative_1}!")
  print(f"{name_2} rolled initiative for {initiative_2}!")
  print("=========================")
  
  if initiative_1 > initiative_2:
    print(f"========== ROUND {round} ==========")
    print(f"{name_1} attack {name_2} for {damage}")
    print(f"{name_2}'s health is down to {health_2 - damage}")
    health_2 = health_2 - damage
    round += 1
    print("=========================")
    time.sleep(2)
    os.system("clear")
    
    if health_2 <= 0:
      print(f"The winner is {name_1}!")
      print(f"{name_2} died in the glory battle!")
      print(f"The battle last for {round} round/s!")
      print("=========================")
      running = False
      
  elif initiative_2 > initiative_1:
    print(f"========== ROUND {round} ==========")
    print(f"{name_2} attack {name_1} for {damage}")
    print(f"{name_1}'s health is down to {health_1 - damage}")
    health_1 = health_1 - damage
    round += 1
    print("=========================")
    time.sleep(2)
    os.system("clear")
    
    if health_1 <= 0:
      print(f"The winner is {name_2}!")
      print(f"{name_1} died in the glory battle!")
      print(f"The battle last for {round} round/s!")
      print("=========================")
      running = False
      
  else:
    print(f"========== ROUND {round} ==========")
    print("They both cross their weapons and block each other's attack!")
    round += 1
    print("=========================")
    time.sleep(2)
    os.system("clear")
