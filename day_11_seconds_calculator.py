print("how many seconds in one year?")
num = int(input("What year is it?: "))
div = int(4)

if num%div == 0:
  print ("This is leap year.")
  a = 1

else:
  print ("This is not leap year.")
  a = 0

sec = 1
minute = 60 * sec
hour = 60 * minute
day = 24 * hour
month = (7 * 31 * day) + (4 * 30 * day) + ((28 + a)) * day

print(month)