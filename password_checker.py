import re
import os

# Define the path to rockyou.txt
ROCKYOU_PATH = os.path.join("Documentation", "rockyou.txt")

def check_strength(password):
    """Checks password strength based on length, uppercase, lowercase, digit, and special character."""
    length = len(password)
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Assigning a score based on the criteria
    if length < 8:
        return "\nVery Weak: Password has to be at least 8 characters long."
    elif not (has_uppercase and has_lowercase and has_digit):
        return "\nWeak: Password has to contain at least one uppercase letter, one lowercase letter, and one digit."
    elif not has_special_char:
        return "\nMedium: Password has to contain at least one special character (e.g., !@#$%^&*)."
    else:
        return "\nStrong: Very good, your password is strong!"

def check_in_rockyou(password):
    """Checks if the password exists in rockyou.txt (a common password list)."""
    if not os.path.exists(ROCKYOU_PATH):
        return "Warning: rockyou.txt file not found. Unable to check password."

    try:
        with open(ROCKYOU_PATH, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                if password.strip() == line.strip():
                    return "\n ⚠️ WARNING: This password is found in the rockyou.txt database. It is not secure!"
        return "\n ✅ Good news: Your password was NOT found in the rockyou.txt list."
    except Exception as e:
        return f"Error reading rockyou.txt: {e}"

def main():
    while True:
        print("\n*** Password Security Checker ***")
        print("1) Check Password Strength")
        print("2) Check if Password Exists in rockyou.txt")
        print("3) Return to Main Menu")
        
        choice = input("\nEnter your choice: ")

        if choice == "1":
            password = input("Enter your password: ")
            print(check_strength(password))

        elif choice == "2":
            password = input("Enter your password: ")
            print(check_in_rockyou(password))

        elif choice == "3":
            break  # Return to main menu

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
