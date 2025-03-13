import re

def get_contact_info():
    phone_number = get_phone_number()
    message = get_message()
    return phone_number, message

def get_phone_number():
    while True:
        phone_number = input("Enter your phone number (format: +65 12345678): ")
        if validate_phone_number(phone_number):
            return phone_number
        else:
            print("Invalid phone number format. Please try again.")

def get_message():
    message = input("Please provide a brief message (optional): ")
    return message

def validate_phone_number(phone_number):
    # Regular expression pattern to match phone numbers in SG format: +65 12345678
    pattern = r"""
        ^             # Start of the string
        \+65          # Country code (+65 for Singapore)
        \s            # Whitespace character (space)
        \d{8}         # 8 digits (the phone number)
        $             # End of the string
    """
    if re.match(pattern, phone_number, re.VERBOSE):
        return True
    else:
        return False

def save_contact_message(phone_number, message):
    with open("contact_messages.txt", "a") as file:
        file.write(f"Phone Number: {phone_number}\n")
        file.write(f"Message: {message}\n\n")
        print("\nThank you for your message!\n")

def main():
    phone_number, message = get_contact_info()
    save_contact_message(phone_number, message)

if __name__ == "__main__":
    main()