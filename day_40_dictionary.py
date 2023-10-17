name = input("Input your name: ").strip().title()
dob = input("Input your date of birth (DD/MM/YYYY): ")
phone = input("Input your phone number (XXX-XXXXXXXX): ")
email = input("Input your email: ")

contact_card = {"name": name, "DOB": dob, "Phone Number": phone, "Email": email}
print(f"""Your name: {contact_card["name"]}""")
print(f"""Your date of birth: {contact_card["DOB"]}""")
print(f"""Your phone number: {contact_card["Phone Number"]}""")
print(f"""Your email: {contact_card["Email"]}""")