print("Test worthy for challenger: Zomboid edition")
print("--------------------------")

score = 0
checking = input("Are you ready?: ")

if checking == "yes":
  answer1 = input("Which city is our home town in Project Zomboid?: ")
  if answer1 == "Westpoint":
    print("Nice!")
    score += 1
  else:
    print("Wrong, man")
    score -= 1

  answer2 = input("Who hoard the gun in AK-47 incident?: ")
  if answer2 == "Neo":
    print("Nice!")
    score += 1
  else:
    print("Wrong, man")
    score -= 1

  answer3 = input("What consider as superfood?: ")
  if answer3 == "Noodle":
    print("Nice!")
    score += 1
  else:
    print("Wrong, man")
    score -= 1

  answer4 = input("Who has the most death count in party?: ")
  if answer4 == "Kopter":
    print("Nice!")
    score += 1
  else:
    print("Wrong, man")
    score -= 1

  answer5 = input("What is that guy weapon of choice?: ")
  if answer5 == "Bolt action rifle":
    print("Nice!")
    score += 1
  else:
    print("Wrong, man")
    score -= 1
else: 
  print("Why are you here then?")

print("Your score is:", score)

