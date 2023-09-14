from caesar_cipher import remove_whitespaces, check_text, caesar_encrypt, caesar_decrypt, check_key2, generate_custom, caesar_encrypt_2keys, caesar_decrypt_2keys

# Main function
def main():
    while True:
        print("Please select an option:")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Double-key encryption")
        print("4. Double-key decryption")
        print("5. Quit")
        option = input("Select option: ")
        
        # Check is the choice is to quit program
        if option == '5':
            break
        
        # Check if the choice is for encryption and proceed accordingly
        if option == '1' or option == '3':
            initial_message = input("Please input the message: ")
            message = remove_whitespaces(initial_message)
            check_text(message)
            key1 = int(input("Please input the first key (from 1 to 25 inclusive ): "))
            if not 1 <= key1 <= 25:
                print("Invalid first key. Please choose a value from 1 to 25.")
                continue
            # The encryption case with only 1 key
            if option == '1':
                encrypted_message = caesar_encrypt(message, key1)
                print("The encryption yields: ", encrypted_message)
            #The encryption case wuth 2 key
            else:
                key2 = input("Please input the second key (minimum 7 characters long ): ")
                key2 = check_key2(remove_whitespaces(key2))
                encrypted_message = caesar_encrypt_2keys(message, key1, key2)
                print("Custom alphabet generated from the second key:", generate_custom(key2))
                print("The encryption with 2 keys yields: ", encrypted_message)
                
        # Check if the choice is for decryption 
        elif option in ['2', '4']:
            encrypted_message = input("Please input the encrypted message: ")
            message = remove_whitespaces(encrypted_message)
            check_text(message)
            key1 = int(input("Please input the first key ( from 1 to 25 inclusive ): "))
            if not 1 <= key1 <= 25:
                print("Invalid first key. Please choose a value from 1 to 25.")
                continue
            # The decryption case with only 1 key
            if option == '2':
                decrypted_message = caesar_decrypt(message, key1)
                print("The decryption yields: ", decrypted_message)
            # The decryption case with 2 keys
            else:
                key2 = input("Please input the second key ( must use only Latin alphabet characters ):")
                key2 = check_key2(remove_whitespaces(key2))
                decrypted_message = caesar_decrypt_2keys(message, key1, key2)
                print("The decryption with 2 keys yields: ", decrypted_message)
        
        else:
            print("Invalid input. Please try again. ")

if __name__ == "__main__":
    encrypted_message = ""
    main()
