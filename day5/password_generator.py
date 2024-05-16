import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ['!', '#', '@', '$', '%', '^', '&', '*', '(', ')', '+']
password = ""
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

for sequence in range(0, nr_letters):
    password += random.choice(letters)

for sequence in range(0, nr_numbers):
    password += random.choice(numbers)

for sequence in range(0, nr_symbols):
    password += random.choice(symbols)
print(f"Easier form: {password}")

password_list = []
for char in password:
    password_list.append(char)
random.shuffle(password_list)

password = ""

for char in password_list:
    password += char
print(f"Harder form: {password}")
