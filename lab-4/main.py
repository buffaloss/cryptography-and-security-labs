import secrets
import re

e_bit_selection = [32, 1, 2, 3, 4, 5,
                    4, 5, 6, 7, 8, 9,
                    8, 9,10,11,12,13,
                   12,13,14,15,16,17,
                   16,17,18,19,20,21,
                   20,21,22,23,24,25,
                   24,25,26,27,28,29,
                   28,29,30,31,32,1]

# for printing the e_bit_selection list
def print_list(arr, num_columns):
    max_length = len(str(max(arr)))
    for i in range(0, len(arr), num_columns):
        row = arr[i:i+num_columns]
        formatted_row = [f"{x:>{max_length}}" for x in row]
        print(' '.join(formatted_row))

# for expanding R(i-1) block from 32 bits to 48
def permute(str):
    permutation = ''
    for i in range(48):
        permutation += str[e_bit_selection[i]-1]
    return permutation

# perform xor operation on 2 strings of the same size (48 bits)
def perform_xor(str1, str2):
    result = ''
    for bit1, bit2 in zip(str1, str2):
        result += '1' if bit1 != bit2 else '0'

    return result

# generating a random K(i) of length 48 bits
def generate_random_k():
    return ''.join(secrets.choice('01') for _ in range(48))

# generation a random R(i-1) of length 32 bits
def generate_random_r():
    return ''.join(secrets.choice('01') for _ in range(32))

# for the user to input K(i) manually
def input_k():
    while True:
        k = input('K(i) (48 bits): ')
        if re.match(r'^[01]{48}$', k):
            return k
        else:
            print('K(i) must have 48 bits and be in binary format (only 0s and 1s). Try again.')

# for  the user to input R(i-1) manually
def input_r():
    while True:
        r = input('R(i-1) (32 bits): ')
        if re.match(r'^[01]{32}$', r):
            return r
        else:
            print('R(i-1) must have 32 bits and be in binary format (only 0s and 1s). Try again.')

while True:
    try:
        print()
        print('Choose action:\n1. Manually input K(i)\n2. Random K(i)\n3. Exit')
        option = int(input('- '))
        if option == 1 or option == 2:
            if option == 1:
                k = input_k()
            elif option == 2:
                k = generate_random_k()
                print(f"Randomly generated K(i): {k}")
            
            print()
            print('1. Manually input R(i-1)\n2. Random R(i-1)\n3. Exit')
            option2 = int(input('- '))
            if option2 == 1 or option2 == 2:
                if option2 == 1:
                    r = input_r()
                elif option2 == 2:
                    r = generate_random_r()
                    print(f"Randomly generated R(i-1): {r}")
                print("E Bit-Selection Table")
                print_list(e_bit_selection,6)
                r = permute(r)
                print(f"E(R(i-1)): {r}")
                result = perform_xor(k,r)
                print(f"B1B2B3B4B5B6B7B8: {result}\nB1: {result[:6]}\nB2: {result[6:12]}\nB3: {result[12:18]}\nB4: {result[18:24]}\nB5: {result[24:30]}\nB6: {result[30:36]}\nB7: {result[36:42]}\nB8: {result[42:248]}")

        elif option == 3:
            exit()
        else:
            print('\nInput is invalid.')

    except ValueError:
        print('\nInvalid input.')