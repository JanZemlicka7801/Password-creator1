import random
import string

def generate_password(length=12, uppercase=True, lowercase=True, numbers=True, symbols=True):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    
    if len(characters) == 0:
        print("Error: You must include at least one type of character.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password length and complexity
length = int(input("Enter the length of the password: "))
uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

# Generate and print the password
generated_password = generate_password(length, uppercase, lowercase, numbers, symbols)
if generated_password:
    print("Generated Password:", generated_password)
