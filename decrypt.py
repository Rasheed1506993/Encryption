from stegano import lsb
from PIL import Image

def decrypt_message(encrypted_message, key):
    # Decrypt the given message using Caesar cipher based on the ASCII sum of the key.
    decrypted_message = ""
    key_shift = sum(ord(char) for char in key) % 26
    for char in encrypted_message:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift - key_shift) % 26 + shift)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char  
    return decrypted_message

def reveal_text_from_image(image_path):
    # Reveal the hidden text inside the image using stegano.lsb library.
    return lsb.reveal(image_path)

def decrypt_text():
    step1 = []
    step2 = []
    step3 = []
    step4 = []
    
    message = ""
    text = input("Enter the path of the virtual message file: ")
    with open(text, 'r') as file:
        message = file.read()
    output_image_path = input("Enter the image file path: ")
    
    secret_text = reveal_text_from_image(output_image_path)
    
    key = input("Enter the decryption key: ")
    
    translated = decrypt_message(secret_text, key)
    
    if len(translated) > len(message):
        while len(message) <= len(translated) - 1:
            message += "€"
    numbers_list = [int(num) for num in translated.split()]
    
    step3 = numbers_list
    for char in message:
        step2.append(ord(char))
        
    for i in range(len(step3)):
        step4.append(step3[i] + step2[i])
    
    print("Decrypted message:")
    for i in range(len(step4)):
        if chr(step4[i]) != '€':
            print(chr(step4[i]), end="")
    print()

# Main program
if __name__ == "__main__":
    decrypt_text()