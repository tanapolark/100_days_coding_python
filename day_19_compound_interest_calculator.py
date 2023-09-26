print("Loan calculator")
principal = int(input("How much do you loan?: "))
loan = principal
rate = int(input("How high is the interest inpercentage?: "))
time = int(input("How many year?: "))

for i in range(time):
  principal += ((principal * rate) / 100)
  print(f"Year {i+1} is ${round(principal,2)}")

print(f"Your total interest is ${round(principal - loan, 2)}!")