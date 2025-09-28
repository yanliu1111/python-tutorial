alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for char in original_text:
        if char in alphabet:
            shifted_position = alphabet.index(char) + shift_amount
            shifted_position %= len(alphabet)  # Wrap around using modulo for example if shift is greater than 26
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += char # Non-alphabet characters are added unchanged
    print(f"The encoded text is {cipher_text}")

# Todo-1: Create a function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# Todo-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
# Todo-3: Combine the encrypt() and decrypt() functions into a single function called caesar().
# Use the 'direction' input to determine whether to encrypt or decrypt the message.

def decrypt(original_text, shift_amount):
    output_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"The decoded text is {output_text}")

decrypt(original_text=text, shift_amount=shift)