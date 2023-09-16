from datetime import date

print("Generation Identifier")

today = date.today()
byear = int(input("Which year were you born?: "))
cyear = int(today.strftime("%Y"))
age = cyear - byear

if 1925 <= byear <= 1946:
  print(f"You are Traditionalists. You are {age} years old")
elif 1947 <= byear <= 1964:
  print(f"You are Baby Boomers. You are {age} years old")
elif 1965 <= byear <= 1981:
  print(f"You are Generation X. You are {age} years old")
elif 1982 <= byear <= 1995:
  print(f"You are Millenials. You are {age} years old")
elif 1996 <= byear <= 2015:
  print(f"You are Generation Z. You are {age} years old")
else:
  print(f"You are Generation Alpha. You are {age} years old")