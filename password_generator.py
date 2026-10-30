
import secrets
import string


def generate_password(length):
    # Letters, numbers and symbols
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    all_characters = letters + numbers + symbols

    # Ensure at least one character from each group
    password_list = [
        secrets.choice(letters),
        secrets.choice(numbers),
        secrets.choice(symbols)
    ]

    # Generate remaining characters
    for _ in range(length - 3):
        password_list.append(secrets.choice(all_characters))

    # Securely shuffle the password
    secrets.SystemRandom().shuffle(password_list)

    # Convert list into string
    return ''.join(password_list)


def main():
    print("=" * 45)
    print("           PASSWORD GENERATOR")
    print("=" * 45)

    # Get password length
    while True:
        try:
            length = int(input("\nEnter password length (minimum 8): "))

            if length < 8:
                print("Error: Password length must be at least 8.")
            else:
                break

        except ValueError:
            print("Error: Please enter a valid number.")

    # Get password quantity
    while True:
        try:
            quantity = int(input("How many passwords do you want? "))

            if quantity < 1:
                print("Error: Quantity must be at least 1.")
            else:
                break

        except ValueError:
            print("Error: Please enter a valid number.")

    # Generate multiple passwords
    print("\n" + "=" * 45)
    print("          GENERATED PASSWORDS")
    print("=" * 45)

    for i in range(quantity):
        password = generate_password(length)
        print(f"Password {i + 1}: {password}")

    print("=" * 45)
    print("Password generation completed successfully!")
    print("Thank you for using Password Generator.")


if __name__ == "__main__":
    main()
