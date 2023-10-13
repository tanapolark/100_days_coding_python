import time
import os

name_list = []
running = True

def screen_clear():
  time.sleep(2)
  os.system("clear")

while running:
  print("Name List:")
  first_name = input("First name: ")
  last_name = input("Last name: ")
  full_name = first_name.title().strip() + " " + last_name.title().strip()
  if full_name not in name_list:
    name_list.append(full_name)
    print(name_list)
    screen_clear()
  else:
    print(f"{full_name} is already in the list.")
    print(name_list)
    screen_clear()