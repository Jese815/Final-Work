def shift_message(message, shift_amount):
    """Shift a message by a given amount."""
    shifted_message = ""
    for char in message:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo
            shifted_char = chr((ord(char) - base + shift_amount) % 26 + base)
            shifted_message += shifted_char
        else:
            # Non-alphabetic characters remain unchanged
            shifted_message += char
    return shifted_message

def make_code():
    """Encode a message."""
    message = input("Enter the message to encode: ")
    shift = int(input("Enter the shift amount: "))
    encoded_message = shift_message(message, shift)
    print("Encoded message:", encoded_message)

def decode_message():
    """Decode a message."""
    message = input("Enter the message to decode: ")
    shift = int(input("Enter the shift amount: "))
    decoded_message = shift_message(message, -shift)
    print("Decoded message:", decoded_message)
    print("Original message (for verification):", shift_message(decoded_message, shift))

def main():
    """Main program loop."""
    while True:
        print("\nMenu:")
        print("1) Make a code")
        print("2) Decode a message")
        print("3) Quit")
        selection = input("Enter your selection: ")

        if selection == "1":
            make_code()
        elif selection == "2":
            decode_message()
        elif selection == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
