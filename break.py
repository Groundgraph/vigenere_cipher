# This unit tries to break the Vigenere cipher by trying to find the key.

from math import sqrt

# Description: This function returns the cosine of the angle between two vectors.
# the vectors are represented as lists of numbers.
# that can be used to find if two vectors are similar.
def cosangle(x,y):
 numerator = 0
 lengthx2 = 0
 lengthy2 = 0
 for i in range(len(x)):
    numerator += x[i]*y[i]
    lengthx2 += x[i]*x[i]
    lengthy2 += y[i]*y[i]
 return numerator / sqrt(lengthx2*lengthy2)

# Description: This function returns the possible key.
# Key length has already been determined.
# encoded string should be much longer than the key length. preferably 1000 times longer.
def get_possible_key(encoded_string, key_length):
    english_frequencies_dict = {
        'a': 0.082, 'b': 0.015, 'c': 0.028, 'd': 0.043, 'e': 0.127, 'f': 0.022, 'g': 0.020, 'h': 0.061, 'i': 0.070, 'j': 0.002, 'k': 0.008, 'l': 0.040, 'm': 0.024, 'n': 0.067, 'o': 0.075, 'p': 0.019, 'q': 0.001, 'r': 0.060, 's': 0.063, 't': 0.091, 'u': 0.028, 'v': 0.010, 'w': 0.023, 'x': 0.001, 'y': 0.020, 'z': 0.001
    }

    english_frequencies = []
    for key in english_frequencies_dict:
        english_frequencies.append(english_frequencies_dict[key])

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


    # create slices of the encoded string based on the key length
    slices = ['']*key_length
    key_index = 0
    for char in encoded_string:
        slices[key_index] += char
        key_index += 1
        if key_index == key_length:
            key_index = 0
    
    frequencies = []
    for i in range(key_length):
        frequencies.append([0]*26)
        for j in range(len(slices[i])):
            char = slices[i][j]
            if char in dict:
                number_for_char = dict[slices[i][j]]
                frequencies[i][number_for_char] += 1
        for j in range(26):
            frequencies[i][j] = frequencies[i][j] / len(slices[i])
    key = ['*']*key_length
    for i in range(key_length):
        for j in range(26):
            testtable = frequencies[i][j:]+frequencies[i][:j]
            if cosangle(english_frequencies,testtable) > 0.9:
                key[i] = reversed_dict[j]
    
    # did we find a character for each slice?
    # convert the key list to a string
    key = ''.join(key)
    
    return key

def get_distances_between_repeated_strings(encoded_string, number_of_chars, distances):
    for i in range(0, len(encoded_string) - number_of_chars):
        substring = encoded_string[i:i+number_of_chars]
        for j in range(i+number_of_chars, len(encoded_string) - number_of_chars):
            if substring == encoded_string[j:j+number_of_chars]:
                distances.append(j-i)
    # make distances unique
    distances = list(set(distances))
    return distances

def get_factors_and_their_fequency(distances):
    factors = {}
    for distance in distances:
        # we ignore key lengths less than 4 and greater than 20
        for i in range(4, 21):
            if distance % i == 0:
                # if factor is already in the dictionary, increment its value
                if i in factors:
                    factors[i] += 1
                else:
                    # add the factor to the dictionary
                    factors[i] = 1
    return factors


# Description: This function returns the possible length of the key.
def get_possible_length_of_key(encryped_string):
    # create a list to hold the distances between repeated strings
    distances = []
    distances = get_distances_between_repeated_strings(encryped_string, 3, distances)
    distances = get_distances_between_repeated_strings(encryped_string, 4, distances)
    distances = get_distances_between_repeated_strings(encryped_string, 5, distances)

    factors = get_factors_and_their_fequency(distances)

    # sort the factors dictionary by value
    sorted_factors = sorted(factors.items(), key=lambda x: x[1], reverse=True)
    
    # keep the top 5 factors
    sorted_factors = sorted_factors[:5]
    return sorted_factors
    
    
def break_vigenere_cipher(encoded_file_name):
    encoded_file = open(encoded_file_name, "r", errors="ignore")
    encoded_string = encoded_file.read()
    encoded_file.close()
    #we will only consider the first 3000 characters to make it faster
    chars_to_consider_for_find_length = 3000
    if len(encoded_string) < 3000:
        chars_to_consider_for_find_length = len(encoded_string)
    smaller_encoded_string = encoded_string[:chars_to_consider_for_find_length]
    possible_length_of_keys = get_possible_length_of_key(smaller_encoded_string)
    
    for length_of_key in possible_length_of_keys:
        print("Possible length of key: " + str(length_of_key[0]))
        # we need string that it is at least 1000 times the length of the key
        length_needed = 1000 * length_of_key[0]
        if length_needed > len(encoded_string):
            length_needed = len(encoded_string)
        encoded_string2 = encoded_string[:length_needed]
        possible_key = get_possible_key(encoded_string2, length_of_key[0])
        # if possible_key contains a *, then we did not find a character for every place in key
        
        if '*' not in possible_key:
            print("Possible key: " + possible_key)
        else:
            # if all are *, then we dound nothing
            if possible_key == '*'*length_of_key[0]:
                print("No possible key found")
            else:    
                print("All possible characters were not found, * represents a missing character")
                print("Possible key: " + possible_key)
        

if __name__ == "__main__":
    encoded_file_name = input("Enter the encoded file name: ")
    break_vigenere_cipher(encoded_file_name)
