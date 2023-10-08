def color(color):
  if color == "red":
    return ("\033[0;31m")
  elif color == "yellow":
    return ("\033[0;33m")
  elif color == "green":
    return ("\033[0;32m")
  elif color == "white":
    return ("\033[0;37m")

title = f"{color('red')}={color('white')}={color('blue')}= {color('yellow')} Music App {color('blue')}={color('white')}={color('red')}="

print(f"       {title: ^35}")

