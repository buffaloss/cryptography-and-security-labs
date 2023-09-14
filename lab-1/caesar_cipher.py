# Define the constant alphabet containing the uppercase Latin alphabet.alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Function to remove spaces and convert message to uppercase.
def remove_whitespaces(message):
    return message.replace(" ", "").upper()

def check_text(message):
    invalid_chars = [char for char in message if char not in alphabet]
    if invalid_chars:
        invalid_chars_str = "', '".join(invalid_chars)
        raise ValueError(f"Invalid character(s) detected: '{invalid_chars_str}'. The text should consist exclusively of Latin alphabet letters.")
    return message

# Function for single-key encryption using the Caesar cipher.
def caesar_encrypt(message, key):
    char_set = alphabet
    encrypted_message = ""
    for char in message:
        char_index = char_set.index(char)
        encrypted_index = (char_index + key) % 26
        encrypted_character = char_set[encrypted_index]
        encrypted_message += encrypted_character
    return encrypted_message

# Function for single-key decryption using the Caesar cipher.
def caesar_decrypt(message, key):
    char_set = alphabet
    decrypted_message = ""
    for char in message:
        character_index = char_set.index(char)
        decrypted_index = (character_index - key) % 26
        decrypted_character = char_set[decrypted_index]
        decrypted_message += decrypted_character
    return decrypted_message

# Function to validate the second key for two-key encryption.
def check_key2(key2):
    if len(key2) < 7:
        raise ValueError("The second key must be at least 7 characters long.")
    invalid_chars = [char for char in key2 if char not in alphabet]
    if invalid_chars:
        invalid_chars_str = "', '".join(invalid_chars)
        raise ValueError(f"The second key contains invalid character(s): '{invalid_chars_str}'. It should consist only of Latin alphabet letters.")
    return key2
    
# Function to generate a shifted alphabet(consisting only of unique characters) based on key2 for two-key encryption.
def generate_custom(key2):
    distinct_chars = ""
    for char in key2:
        if char not in distinct_chars:
            distinct_chars += char
    custom_alphabet = distinct_chars
    for char in alphabet:
        if char not in distinct_chars:
            custom_alphabet += char
    return custom_alphabet

# Function for two-key encryption using the Caesar cipher.
def caesar_encrypt_2keys(message, key1, key2):
    encrypted_message = caesar_encrypt(message, key1)
    encrypted_message_2key = ""
    char_set = alphabet
    encrypted_key2 = generate_custom(key2)
    for char in encrypted_message:
        index = char_set.index(char)
        encrypted_message_2key += encrypted_key2[index]
    return encrypted_message_2key

# Function for two-key decryption using the Caesar cipher.
def caesar_decrypt_2keys(message, key1, key2):
    char_set = alphabet
    encrypted_key2 = generate_custom(key2)
    decryption_partial = ""
    for char in message:
        index = encrypted_key2.index(char)
        decryption_partial += char_set[index]
    return caesar_decrypt(decryption_partial, key1)
