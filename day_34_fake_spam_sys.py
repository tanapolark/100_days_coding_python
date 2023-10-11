import os
import time
import random

email_list = []
running = True

while running:
  print("SPAMMER Inc.")
  menu = input(f"1. Add Email\n2. Remove email\n3. Show email\n4. Get SPAMMING\n")
  
  if menu == "1":
    email = input("Enter email: ")
    if email not in email_list:
      email_list.append(email)
    else:
      print("This email already in the list")
      
  if menu == "2":
    email = input("Enter email: ")
    if email in email_list:
      email_list.remove(email)
    else:
      print("This email not in the list")

  if menu == "3":
    print(email_list)

  if menu == "4":
    print(f"Dear {email_list[:]}, Your email is SPAMMING")
    time.sleep(random.randint(1, 5))
    print("It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.")
    time.sleep(random.randint(1, 5))
    print("Love and hugs,\nIan Spammington III")
    time.sleep(5)
    os.system("cls")