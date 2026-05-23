alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    encrypted_message = ""
    for char in original_text:
        position = alphabet.index(char)
        position += shift_amount
        if position > 25:
            position -= 26
        encrypted_message +=alphabet[position]
    print(f"Encrypted message: {encrypted_message}")

encrypt(text, shift)