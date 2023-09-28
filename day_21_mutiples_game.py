print("Math game")

running = True

while running:
  score = 0
  multiple = int(input("Name your multiples: "))
  rounds = int(input("How many round: "))
  
  for round in range(rounds):
    answer = int(input(f"{round + 1} * {multiple} = "))
    
    if answer == ((round + 1) * multiple):
      print("good job")
      score += 1
    else:
      print("wrong")
      score -= 1

  print(f"You score is {score}")
  
  if input("do you want to play again? (y/n): ") == "n":
    running = False
    print("Thanks for playing!")
