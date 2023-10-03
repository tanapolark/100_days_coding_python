from replit import audio
import os
import time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    if input("Pause? (y/n): ") == "y":
      source.paused = True

while True:
  # clear the screen 
  os.system("clear")
  # Show the menu
  print("🎵 MyPOD Music Player")
  print("")
  print("Press y to Play")
  print("Press n to Exit")
  # take user's input
  # check whether you should call the play() subroutine depending on user's input
  if input("Do you want to play the music? (y/n): ") == "y":
    play()
