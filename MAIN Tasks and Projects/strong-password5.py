import random
import string


# Common weak passwords
COMMON_PASSWORDS = {
    "password",
    "password123",
    "12345678",
    "123456789",
    "qwerty",
    "qwerty123",
    "admin",
    "admin123",
    "welcome",
    "letmein"
}


def has_repeated_characters(password):
    """Check if any character appears more than once."""

    characters = set()

    for char in password.lower():

        if char in characters:
            return True

        characters.add(char)

    return False


def check_common_password(password):
    """Check whether password is a commonly used weak password."""

    return password.lower() in COMMON_PASSWORDS


def contains_name(password, name):
    """Check whether password contains the user's name."""

    if not name:
        return False

    return name.lower() in password.lower()


def check_password(password, name):

    score = 0
    feedback = []

    # -------------------------
    # 1. Length
    # -------------------------

    if len(password) >= 8:
        score += 20
    else:
        feedback.append(
            "Use at least 8 characters."
        )

    if len(password) >= 12:
        score += 10

    # -------------------------
    # 2. Uppercase
    # -------------------------

    if any(char.isupper() for char in password):
        score += 15
    else:
        feedback.append(
            "Add at least one uppercase letter."
        )

    # -------------------------
    # 3. Lowercase
    # -------------------------

    if any(char.islower() for char in password):
        score += 15
    else:
        feedback.append(
            "Add at least one lowercase letter."
        )

    # -------------------------
    # 4. Number
    # -------------------------

    if any(char.isdigit() for char in password):
        score += 15
    else:
        feedback.append(
            "Add at least one number."
        )

    # -------------------------
    # 5. Special character
    # -------------------------

    if any(char in string.punctuation for char in password):
        score += 15
    else:
        feedback.append(
            "Add at least one special character."
        )

    # -------------------------
    # 6. Repeated characters
    # -------------------------

    if has_repeated_characters(password):

        score -= 10

        feedback.append(
            "Avoid repeated characters."
        )

    # -------------------------
    # 7. Common password
    # -------------------------

    if check_common_password(password):

        score = 0

        feedback.append(
            "This is a commonly used password."
        )

    # -------------------------
    # 8. Name inside password
    # -------------------------

    if contains_name(password, name):

        score -= 10

        feedback.append(
            "Avoid using your name in the password."
        )

    # Keep score between 0 and 100
    score = max(0, min(score, 100))

    # -------------------------
    # Strength
    # -------------------------

    if score >= 90:
        strength = "Excellent"

    elif score >= 75:
        strength = "Very Strong"

    elif score >= 60:
        strength = "Strong"

    elif score >= 40:
        strength = "Medium"

    elif score >= 20:
        strength = "Weak"

    else:
        strength = "Very Weak"

    return score, strength, feedback


def generate_password(length=12):

    if length < 4:
        raise ValueError(
            "Password length must be at least 4."
        )

    # Guarantee one character from each category

    password_characters = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Remaining characters

    all_characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    for _ in range(length - 4):

        password_characters.append(
            random.choice(all_characters)
        )

    # Shuffle the characters so the first
    # four aren't always predictable

    random.shuffle(password_characters)

    return "".join(password_characters)


def main():

    while True:

        print("\n========== PASSWORD SECURITY TOOL ==========")

        print("1. Check Password")
        print("2. Generate Strong Password")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        # --------------------------------
        # CHECK PASSWORD
        # --------------------------------

        if choice == "1":

            name = input("Enter your name: ")

            password = input(
                "Enter your password: "
            )

            score, strength, feedback = check_password(
                password,
                name
            )

            print("\n========== PASSWORD ANALYSIS ==========")

            print(f"Score    : {score}/100")
            print(f"Strength : {strength}")

            if feedback:

                print("\nSuggestions:")

                for item in feedback:
                    print("-", item)

            else:

                print(
                    "\nExcellent! "
                    "Your password passed all checks."
                )

        # --------------------------------
        # GENERATE PASSWORD
        # --------------------------------

        elif choice == "2":

            try:

                length = int(
                    input(
                        "Enter password length: "
                    )
                )

                if length < 8:

                    print(
                        "For better security, "
                        "use at least 8 characters."
                    )

                    continue

                password = generate_password(length)

                print(
                    "\nGenerated Strong Password:"
                )

                print(password)

            except ValueError as e:

                print("Error:", e)

        # --------------------------------
        # EXIT
        # --------------------------------

        elif choice == "3":

            print("Goodbye!")

            break

        else:

            print(
                "Invalid choice. Please try again."
            )


main()