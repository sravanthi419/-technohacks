import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_custom_password(char_length, num_length, symbol_length):
    alpha_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeric_chars = "0123456789"
    symbol_chars = "!@#$%^&*()"

    selected_alpha = random.sample(alpha_chars, char_length)
    selected_numeric = random.sample(numeric_chars, num_length)
    selected_symbols = random.sample(symbol_chars, symbol_length)

    password_list = selected_alpha + selected_numeric + selected_symbols
    random.shuffle(password_list)
    
    generated_password = ''.join(password_list)
    return generated_password

# Generate a random password
random_password = generate_random_password(8)
print("Randomly generated password:", random_password)

# Generate a custom password
char_length = int(input("Enter the number of characters in your password: "))
num_length = int(input("Enter the number of numbers in your password: "))
symbol_length = int(input("Enter the number of symbols in your password: "))

custom_password = generate_custom_password(char_length, num_length, symbol_length)
print("The custom-generated password is:", custom_password)