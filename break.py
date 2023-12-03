# This unit tries to break the Vigenere cipher by trying to find the key.

def get_distances_between_repeated_strings(encoded_string, number_of_chars, factors):
    distances = []
    for i in range(0, len(encoded_string) - number_of_chars):
        substring = encoded_string[i:i+number_of_chars]
        for j in range(i+number_of_chars, len(encoded_string) - number_of_chars):
            if substring == encoded_string[j:j+number_of_chars]:
                distances.append(j-i)
    # make distances unique
    distances = list(set(distances))
    for distance in distances:
        for i in range(2, distance):
            if distance % i == 0:
                # if factor is already in the dictionary, increment its value
                if i in factors:
                    factors[i] += 1
                else:
                    # add the factor to the dictionary
                    factors[i] = 1
    
    
    # sort the sorted_factors dictionary by value
    return factors


# Description: This function returns the possible length of the key.
def get_possible_length_of_key(encryped_string):
    # create a dictionary to hold the factors and their frequency
    factors = {}
    factors = get_distances_between_repeated_strings(encryped_string, 3, factors)
    factors = get_distances_between_repeated_strings(encryped_string, 4, factors)
    factors = get_distances_between_repeated_strings(encryped_string, 5, factors)

    # sort the factors dictionary by value
    sorted_factors = sorted(factors.items(), key=lambda x: x[1], reverse=True)
    print(sorted_factors)

def break_vigenere_cipher(encoded_file_name):
    encoded_file = open(encoded_file_name, "r", errors="ignore")
    encoded_string = encoded_file.read()
    encoded_file.close()
    #we will only consider the first 3000 characters
    encoded_string = encoded_string[:3000]
    get_possible_length_of_key(encoded_string)

if __name__ == "__main__":
    encoded_file_name = input("Enter the encoded file name: ")
    break_vigenere_cipher(encoded_file_name)
