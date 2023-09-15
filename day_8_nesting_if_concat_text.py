print("The ultimate insult generator")
print("-----------------------------")

print("I'll not respond for any emotional damage you receive")

checking = input("Are you sure to coutinue?: ")
if checking == "Yes" or checking == "yes":
  name = input("Who are you?: ")
  activity = input("What do you like to do?: ")
  favthing = input("Thing you like?: ")

  print(f"You are {name} the enjoyer of {activity} because your parents never play with you. The only time they give {favthing} to you because you are annoying and it eventaully become your best friend.")
else:
  print("Smart Choice")
  checking2 = input("Afraid or need some love?: ")
  if checking2 == "Afraid":
    print("Coward")
  else:
    print("I love you")