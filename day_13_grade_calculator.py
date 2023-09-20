print("Exam Grade Calculator")
print("Please input your score.")

max = int(input("Max point possible: "))
score = int(input("Your points: "))
grade = round(score * (100 / max), 2)

print(f"You got {grade}%.")

if score > max:
  print("The score cannot exceed the maximum score")
  print("Please try again")
else:
  if grade >= 90:
    print("You get A+")
  elif grade >= 80:
    print("You get A")
  elif grade >= 70:
    print("You get B")
  elif grade >= 60:
    print("You get C")
  elif grade >= 50:
    print("You get D")
  else:
    print("You get F")
