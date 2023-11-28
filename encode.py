# Description: This file contains the function that encodes a file using a key 
# using the Vigenere cipher.
def encode(input_file, output_file, key):
    # Open the input file for reading
    input_file = open(input_file, "r")
    # Open the output file for writing
    output_file = open(output_file, "w")
    # Read the input file into a string
    input_string = input_file.read()
    # Close the input file
    input_file.close()
    # Create a string to hold the encoded message
    encoded_message = ""
    # Create a variable to hold the index of the key
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
    
    # convert key to lowercase
    key = key.lower()
    # convert input string to lowercase
    input_string = input_string.lower()

    for char in input_string:
        if char in dict:
            number_for_key = dict[key[key_index]]
            number_for_char = dict[char]
            encoded_number = (number_for_key + number_for_char) % 26
            encoded_char = reversed_dict[encoded_number]
            encoded_message += encoded_char
        else:
            encoded_char = char
            encoded_message += encoded_char
        key_index += 1
        if key_index == len(key):
            key_index = 0
    
    # write the encoded message to the output file
    output_file.write(encoded_message)
    # Close the output file
    output_file.close()

if __name__ == "__main__":
    # get the input file name from the user
    input_file = input("Enter the input file name: ")
    # get the output file name from the user
    output_file = input("Enter the output file name: ")
    # get the key from the user
    key = input("Enter the key: ")
    # encode the file
    encode(input_file, output_file, key)