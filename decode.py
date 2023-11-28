
def decode(infile, outfile, key):
    """Decode a file using a key using vigenere cipher"""
    infile = open(infile, 'r')
    outfile = open(outfile, 'w')
    encoded_str = infile.read()
    infile.close()
    chartoint = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6,
                        "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13,
                        "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20,
                        "v":21, "w":22, "x":23, "y":24, "z":25}
    inttochar = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g",
                        7:"h", 8:"i", 9:"j", 10:"k", 11:"l", 12:"m", 13:"n",
                        14:"o", 15:"p", 16:"q", 17:"r", 18:"s", 19:"t", 20:"u",
                        21:"v", 22:"w", 23:"x", 24:"y", 25:"z"}
    plaintext = ""
    key = key.lower()
    key_index = 0
    for char in encoded_str:
        if char in chartoint:
            key_char = key[key_index]
            key_number = chartoint[key_char]
            char_number = chartoint[char]
            decode_number = (char_number - key_number) % 26
            decode_char = inttochar[decode_number]
            plaintext += decode_char
        else:
            plaintext += char
        key_index += 1
        if key_index == len(key):
            key_index = 0

    outfile.write(plaintext)
    
    outfile.close()

if __name__ == "__main__":
    # get the input file name from the user
    input_file = input("Enter the input file name: ")
    # get the output file name from the user
    output_file = input("Enter the output file name: ")
    # get the key from the user
    key = input("Enter the key: ")
    # encode the file
    decode(input_file, output_file, key)