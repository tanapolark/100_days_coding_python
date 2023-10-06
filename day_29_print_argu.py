def color(color, word):
  if color == red:
    print("\033[31m", word, sep="", end="")
  if color == purple:
    print("\033[0;35m", word, sep="", end="")
  if color == cyan:
    print("\033[0;36m", word, sep="", end="")

print("Super Subroutine")

print(f"With my {color(purple, new program)} I can just call color(and , red) {color(red, and)} that word will appear in the color I set it to.")

print(f"With no {color(cyan, weird gap)}.")