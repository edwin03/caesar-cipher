from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def encrypt(original_text, shift_amount):
    encrypted_message = ""
    for char in original_text:
        if char in alphabet:
            position = alphabet.index(char) + shift_amount
            position %= len(alphabet)
            encrypted_message +=alphabet[position]
        else:
            encrypted_message += char
    print(f"Encrypted message: {encrypted_message}")

def decrypt(original_text, shift_amount):
    decrypted_message = ""
    for char in original_text:
        if char in alphabet:
            position = alphabet.index(char) - shift_amount
            position %= len(alphabet)
            decrypted_message += alphabet[position]
        else:
            decrypted_message += char
    print(f"Decrypted message: {decrypted_message}")

def caesar(direction, text, shift):
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid selction. Try again.")

stop = False
while not stop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    cont = input("Type 'yes' if you want to go again. otherwise type 'no':\n").lower()
    if cont == 'no':
        print("Goodbye!")
        stop = True