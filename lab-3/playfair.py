
def create_matrix(key):
    key = ''.join(dict.fromkeys(key.upper().replace('J', 'I')))
    alphabet = 'AĂÂBCDEFGHIÎKLMNOPQRSȘTȚUVWXYZ'
    matrix = [char for char in key if char in alphabet] + list(alphabet)
    return ''.join(matrix[i] if matrix[i] not in matrix[:i] else '' for i in range(len(matrix)))

def prepare_text(text):
    text = ''.join(filter(str.isalpha, text.upper())).replace('J', 'I')
    return text if len(text) % 2 == 0 else text + 'X'

def get_pairs(text):
    return [text[i:i+2] for i in range(0, len(text), 2)]

def cipher(plain_text, key_matrix, shift):
    text = prepare_text(plain_text)
    pairs = get_pairs(text)
    cipher_text = ''
    for pair in pairs:
        row1, col1 = divmod(key_matrix.index(pair[0]), 5)
        row2, col2 = divmod(key_matrix.index(pair[1]), 5)
        if row1 == row2:
            cipher_text += key_matrix[row1 * 5 + (col1 + shift) % 5]
            cipher_text += key_matrix[row2 * 5 + (col2 + shift) % 5]
        elif col1 == col2:
            cipher_text += key_matrix[((row1 + shift) % 5) * 5 + col1]
            cipher_text += key_matrix[((row2 + shift) % 5) * 5 + col2]
        else:
            cipher_text += key_matrix[row1 * 5 + col2]
            cipher_text += key_matrix[row2 * 5 + col1]
    return cipher_text


def encrypt(plain_text, key_matrix):
    return cipher(plain_text, key_matrix, 1)

def decrypt(cipher_text, key_matrix):
    return cipher(cipher_text, key_matrix, -1)

def print_matrix(matrix):
    for i in range(0, len(matrix), 5):
        print(matrix[i:i+5])
    


def main():
    print()
    print("Playfair Cipher")
    key = input("Enter the key (at least 7 characters): ")
    while len(key) < 7:
        print("Key must be at least 7 characters long.")
        key = input("Enter the key (at least 7 characters): ")

    key_matrix = create_matrix(key)

    while True:
        print("\nMenu:")
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            plain_text = input("Enter the message to encrypt: ")
            print("Encrypted Text:", encrypt(plain_text, key_matrix))
            print()
            print("Key Matrix:")
            print_matrix(key_matrix)
            
        elif choice == '2':
            cipher_text = input("Enter the cryptogram to decrypt: ")
            print("Decrypted Text:", decrypt(cipher_text, key_matrix))
            print()
            print("Key Matrix:")
            print_matrix(key_matrix)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()