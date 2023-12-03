# Description: This file contains the function that decrypts a file using a key 
# using the Vigenere cipher.
def decrypte(encoded_file_name, decoded_file_name, key):
    encoded_file = open(encoded_file_name, "r", errors="ignore")
    decoded_file = open(decoded_file_name, "w")
    encoded_string = encoded_file.read()
    encoded_file.close()
    decoded_message = ""
    key_index = 0

    dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
            'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
            'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20,
            'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
    
    reversed_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 
                     5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 
                     10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 
                     15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 
                     20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 
                     25: 'z'}
    
    for character in encoded_string:
        if character in dict:
            key_char = key[key_index]
            number_for_key = dict[key_char]
            number_for_char = dict[character]
            decoded_number = (number_for_char - number_for_key)
            if decoded_number < 0:
                decoded_number += 26
            decoded_char = reversed_dict[decoded_number]
            decoded_message += decoded_char
        else:
            decoded_char = character
            decoded_message += decoded_char
        key_index += 1
        if key_index == len(key):
            key_index = 0

    decoded_file.write(decoded_message)
    decoded_file.close()

if __name__ == "__main__":
    encoded_file_name = input("Enter the encrypted file name: ")
    decoded_file_name = input("Enter the decrypted name: ")
    key = input("Enter the key: ")
    decrypte(encoded_file_name, decoded_file_name, key)