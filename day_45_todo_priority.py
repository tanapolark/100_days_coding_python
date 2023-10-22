import time
import os

toDoList = []

def add():
  time.sleep(1)
  os.system("clear")
  task = input("What is the task?: ")
  date = input("When is it due by?: ")
  priority = input("What is the priority?: ").capitalize()
  print(task, date, priority, end = " | ")
  row = [task, date, priority]
  toDoList.append(row)
  
def remove():
  time.sleep(1)
  os.system("clear")
  find = input("Name of To-do List to remove > ")
  for row in toDoList:
    if find in row:
      toDoList.remove(row)

def edit():
  time.sleep(1)
  os.system("clear")
  find = input("Name of To-do List to edit > ")
  found = False
  for row in toDoList:
    if find in row:
      found = True
  if not found:
    print("Couldn't find that")
    return
  for row in toDoList:
    if find in row:
      toDoList.remove(row)
  name = input("Name > ")
  date = input("Due Date > ")
  priority = input("Priority > ").capitalize()
  row = [name, date, priority]
  toDoList.append(row)
  print("Added")

def view():
  time.sleep(1)
  os.system("clear")
  options = input("1: All\n2: By Priority\n> ")
  if options=="1":
    for row in toDoList:
      for item in row:
        print(item, end=" | ")
      print()
    print()
  else:
    priority = input("What priority? > ").capitalize()
    for row in toDoList:
      if priority in row:
        for item in row:
          print(item, end=" | ")
        print()
    print()
  time.sleep(1)

while True:
  menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    edit()
  else:
    remove()
  time.sleep(1)
  os.system("clear")