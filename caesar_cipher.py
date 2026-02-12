alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            shifted_position = (position + shift_amount) % len(alphabet)
            encrypted_text += alphabet[shifted_position]
        else:
            encrypted_text += letter
    print(f"Here's the encoded result: {encrypted_text}")

def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            shifted_position = position - shift_amount
            shifted_position %= len(alphabet)
            decrypted_text += alphabet[shifted_position]
        else:
            decrypted_text += letter
    print(f"Here's the decoded result: {decrypted_text}")

def caesar(input_direction):
    
    if input_direction == "encode":
        encrypt(original_text=text, shift_amount=shift)
    elif input_direction == "decode":
        decrypt(original_text=text, shift_amount=shift)
    else:
        print("Invalid input")

caesar(direction)
