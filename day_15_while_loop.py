animal = None
running = True

while running:
  animal = str(input("What animal do you want?: ")).lower() 

  if animal == "cow":
    print("A cow goes moo.")
  elif animal == "lemur":
    print("Ummm...the Lesser Spotter Lemur goes awooga.")
  else:
    print("I'm not that smart.")
  
  if input("Do you want to exit? (y/n): ") == "y":
    print("Thanks for playing!")
    running = False
  