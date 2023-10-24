import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password geenerator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

password = ""
pass_list = []

for char in range(1, num_letters + 1):
    # password += random.choice(letters)
  pass_list.append(random.choice(letters))
for char in range(1, num_symbols + 1):
    # password += random.choice(symbols)
  pass_list.append(random.choice(symbols))
for char in range(1, num_numbers + 1):
  pass_list.append(random.choice(numbers))
    # password += random.choice(numbers)
# print(password)
# print(pass_list)
for _ in range(1, len(pass_list) + 1):
  password += random.choice(pass_list)
print(f"Your newly generated password is: {password}")
