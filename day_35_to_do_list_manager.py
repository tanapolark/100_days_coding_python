import time
import os

to_do_list = []
running = True

def clear():
  time.sleep(2)
  os.system("clear")

while running:
  print("To Do List Manager:")
  menu = input("1. Add activity\n2. Delete activity\n3. View list\n4. Edit activity\n")
  
  if menu == "1":
    activity = input("Please enter your activity: ")
    if activity not in to_do_list:
      to_do_list.append(activity)
      print(to_do_list)
      clear()
    else:
      print(f"{activity} is already in the list.")
      clear()

  if menu == "2":
    activity = input("Please enter your activity: ")
    if activity in to_do_list:
      confirm = input("Do you really want to delete this activity? (y/n): ")
      if confirm == "y":
        to_do_list.remove(activity)
        print(to_do_list)
        clear()
    else:
      print(f"{activity} is already not in the list.")
      clear()

  if menu == "3":
    print(to_do_list)
    clear()

  if menu == "4":
    print(to_do_list)
    sub_menu = input("Do you want to edit or remove the list?: ")
    if sub_menu == "edit":
      index = int(input("Which index do you want to edit?: "))
      new_activity = input("What is the new activity?: ")
      to_do_list[index - 1] = new_activity
      print(to_do_list)
      clear()
    elif sub_menu == "remove":
      confirm = input("Do you really want to delete this list? (y/n): ")
      if confirm == "y":
        to_do_list = []
        print(to_do_list)
        clear()
    