import random

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special = "!@#$%^&*"

password = ""
for i in range(3):
    password += random.choice(letters)
for x in range(3):
    password += random.choice(digits)
for z in range(2):
    password += random.choice(special)
print(password)
