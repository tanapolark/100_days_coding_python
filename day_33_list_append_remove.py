to_do_list = []

def printlist():
  print()
  print(to_do_list)

while True:
  print("To Do List Manager:")
  menu = input("Do you want to view, add, or remove your to do list?: ")
  if menu == "view":
    printlist()
  elif menu == "add":
    item = input("What do you want to add?: ")
    to_do_list.append(item)
    printlist()
  elif menu == "remove":
    item = input("What do you want to remove?: ")
    if item in to_do_list:
      to_do_list.remove(item)
      printlist()
    else:
      print(f"{item} is not in the list.")