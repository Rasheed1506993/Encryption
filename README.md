### Encrypting and Hiding Messages in Images Using Steganography and Caesar Cipher

# Project Title
**Encrypt and Hide Messages in Images**

## Project Description
This project provides a secure way to encrypt messages and hide them inside images using a combination of Caesar Cipher for encryption and Steganography for hiding the encrypted message within an image. The project includes both encryption and decryption functionalities.

## Features
- **Message Encryption**: Encrypts a message using a key with Caesar Cipher.
- **Message Hiding**: Hides the encrypted message inside an image using Steganography.
- **Message Decryption**: Decrypts the hidden message from the image using the provided key.
- **Message Revealing**: Extracts the hidden message from the image.

## How It Works
1. **Encryption Process**:
    - The user provides a message and a virtual message file.
    - Both messages are padded to ensure they are of equal length.
    - ASCII values of both messages are used to create a unique encrypted key.
    - The user provides an encryption key that must be 8 characters long and include letters, numbers, and symbols.
    - The encrypted message is generated and hidden within an image file using Steganography.

2. **Decryption Process**:
    - The hidden message is extracted from the image.
    - The user provides the decryption key.
    - The decrypted message is revealed and displayed to the user.

## Requirements
- Python 3.x
- `stegano` library
- `Pillow` library

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/Rasheed1506993/Encryption.git
    cd Encryption
    ```

2. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
### Encryption
1. Run the `crypto_text` function to encrypt and hide the message.
    ```sh
    python encrypt.py
    ```
2. Follow the on-screen instructions to provide:
    - The path to the file containing the message to be encrypted.
    - The path to the virtual message file.
    - The encryption key.
    - The image file where the encrypted message will be hidden.

### Decryption
1. Run the `decrypt_text` function to reveal and decrypt the hidden message.
    ```sh
    python decrypt.py
    ```
2. Follow the on-screen instructions to provide:
    - The path to the virtual message file.
    - The image file from which the message will be extracted.
    - The decryption key.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
- The `stegano` library for image steganography.
- The `Pillow` library for image processing.
- Python for being an awesome programming language.