print("Bill spliter")

myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = int(input("How much tip do you give in percentage?: "))
total = myBill + ((myBill * tip) / 100)
split = total / numberOfPeople
answer = round(split, 2)
print("You all owe", answer)1499