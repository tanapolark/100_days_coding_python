print("Star wars name generator")

first_name = input("Input your first name: ")
last_name = input("Input your last name: ")
pet_name = input("Input your pet name: ")
city_name = input("Input your city name: ")

new_first_name = first_name[:4].title() + last_name[:4]
new_last_name = pet_name[:4] + city_name[:4]

print(f"Your Star Wars name is {new_first_name} {new_last_name}")