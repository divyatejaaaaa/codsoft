import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters for strength."

    # Characters to use in password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters from the list
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("===== PASSWORD GENERATOR =====")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print(f"\n🔐 Your generated password is:\n{password}")
    except ValueError:
        print("Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    main()
