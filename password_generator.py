import random
import string

print("---- PASSWORD GENERATOR ----")

# Ask user for password length
length = int(input("Enter the desired password length: "))

# Characters used in password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display password
print("\nGenerated Password:", password)