print("list generator")

start = int(input("Start at: "))
end = int(input("End before: "))
increment = int(input("Increment between values: "))

for start in range(start, end, increment):
  print(start)