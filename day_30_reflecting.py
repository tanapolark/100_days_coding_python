print("30 Days - What did you think?\n")
for i in range(1,31):
  feedback = input(f"Day {i} : \n")
  response = f"You thought Day {i} is {Feedback}"
  print(f"\033[32m {Response:^50} \033[0m")