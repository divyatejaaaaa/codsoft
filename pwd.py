import secrets
import string


def password_generator():
    print("🔑 Secure Password Generator 🔑")

    # Ask user for length
    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    if length < 4:
        print("❌ Password length should be at least 4.")
        return

    # Define character pools
    options = {
        "Lowercase Letters": string.ascii_lowercase,
        "Uppercase Letters": string.ascii_uppercase,
        "Digits": string.digits,
        "Special Characters": "!@#$%^&*()-_=+[]{}|;:,.<>?/`~"
    }

    # Ask user preferences
    chosen_pools = []
    for category, chars in options.items():
        choice = input(f"Include {category}? (y/n): ").strip().lower()
        if choice == "y":
            chosen_pools.append(chars)

    if not chosen_pools:
        print("❌ You must select at least one character type.")
        return

    # Ensure at least one char from each chosen pool
    password = [secrets.choice(pool) for pool in chosen_pools]

    # Fill the remaining characters
    all_chars = "".join(chosen_pools)
    password += [secrets.choice(all_chars) for _ in range(length - len(password))]

    # Shuffle password securely
    secrets.SystemRandom().shuffle(password)

    # Convert list to string
    final_password = "".join(password)

    print(f"\n✅ Generated Password: {final_password}")


# Run program
if __name__ == "__main__":
    password_generator()
