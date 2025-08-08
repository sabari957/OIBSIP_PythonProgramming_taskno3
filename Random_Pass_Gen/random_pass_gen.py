import random
import string

def get_user_preferences():
    length=int(input("Enter the password length:"))
    use_letters = input("Include letters? (y/n):").lower()=='y'
    use_numbers = input("Include numbers? (y/n):").lower()=='y'
    use_symbols = input("Include symbols? (y/n):").lower()=='y'

    return length,use_letters,use_numbers,use_symbols

def build_character_pool(use_letters,use_numbers,use_symbols):
    characters=''
    if use_letters:
        characters+=string.ascii_letters  #abc
    if use_numbers:
        characters+=string.digits         #0123
    if use_symbols:
        characters+=string.punctuation    #!@#.
    return characters

def generate_password(length,characters):
    if not characters:
        return "Error: No character set selected...!"
    password=''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔒Welcome to the Password Generator🔑")
    length,use_letters,use_numbers,use_symbols=get_user_preferences()
    characters=build_character_pool(use_letters,use_numbers,use_symbols)
    password=generate_password(length,characters)

    print(f"\nYour generated password: {password}")

if __name__=="__main__":
    main()