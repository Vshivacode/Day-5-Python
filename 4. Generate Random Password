# Random Password Generator
import random

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# Numbers will be in quotes because when concatinating numbers we want them to display side by side instead of addition
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   # Read comment above
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "<", ">", "/"]

user_alphabets = int(input("how many alphabets do you want in password: "))
user_numbers = int(input("how many numbers do you want in password: "))
user_symbols = int(input("how many symbols do you want in password: "))
password = []
for let in range(0, user_alphabets):
    password += random.choice(alphabets)
for num in range(0, user_numbers):
    password += random.choice(numbers)
for sym in range(0, user_symbols):
    password += random.choice(symbols)
# print(password)     # Before shuffle
random.shuffle(password)
result = ""
for res in password:
    result += res
print(f'Your Random Password is: "{result}"')


# Output:
how many alphabets do you want in password: 5
how many numbers do you want in password: 8
how many symbols do you want in password: 4
Your Random Password is: "t33v5Z_R<26_8^4J3"
