counter = 0
running = True

print("Fill in the blank lyrics!")
print("Type in the blank lyrics and see if you are as cool as me.")

while running:
  print("Never going to ______ you up.")
  answer = input(": ").lower()
  if answer == "give":
    print(f"Well done! It only took you {counter} attempt/s.")
    if input("Play again? (y/n): ").lower() == "n":
      running = False
  else:
    print("Nope, try again.")
    counter += 1

