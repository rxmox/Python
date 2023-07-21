# encryption.py
# Omar Ahmed, ENDG 233 F21
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# You may optionally import the string module from the standard Python library. No other modules may be imported.
# Remember to include docstrings for your functions and comments throughout your code.




### Define your functions here
def check_validity(cipher):
    if len(set(cipher)) == 26 and cipher.isalnum():
        return True
    return False

def encode_text(cipher):
    dictionary = {}
    for i in range(len(cipher)-1):
        if i == len(cipher) - 1:
            dictionary[cipher[i]] = cipher[0]
        else:
            dictionary[cipher[i]] = cipher[i+1]
    return dictionary

def generate_encrypted_text(text,dictionary):
    list = []
    for char in text:
        list.append(dictionary[char])
    return "".join(list)

def get_key(code,dictionary):
    for encryption, char in dictionary.items():
        if code == char:
            return encryption

def decode_text(dictionary,text):
    new_text = ""
    for char in text:
        addition = get_key(char,dictionary)
        new_text = new_text + addition
    return new_text


print("ENDG 233 Encryption Program")

### Add your main program code here
intro_text = ("What would you like to do?\n"
             "1: Encode text\n"
             "2: Decode text\n"
             "0: End the program\n"
             "Input: ")

while True:
    user_input = int(input(intro_text))
    if user_input == 0:
        break
    if user_input == 1:
        text = input("Please enter the text to be processed: ")
        while True:
            cipher = input("Please enter cipher text: ").lower()                             
            if check_validity(cipher):
                break
            print("Your cipher must contain 26 unique elements of a-z or 0-9\n")  
        print('Your cipher is valid.')
        dictionary = encode_text(cipher)
        encrypted_text = generate_encrypted_text(text, dictionary)
        print("Your output is:", encrypted_text, "\n")
    if user_input == 2:
        text_to_decode = input("Please enter the text to be processed: ")
        while True:
            cipher = input("Please enter cipher text: ")
            if check_validity(cipher):
                break
            print("Your cipher must contain 26 unique elements of a-z or 0-9\n")
        dictionary = encode_text(cipher)
        decoded_text = decode_text(dictionary, text_to_decode)
        print("Your output is:", decoded_text, "\n")
        
print('Thank you for using the encryption program.')

"""
-----Demonstrate that duplicate values are removed while maintaining given element order
set(cipher)
#set removes duplicates

"""
#bcdefghijklmnopqrstuvwxyza

# Code does not work when cipher contains numbers

# code is supposed to remove duplicates from cipher and run normally

# does not encode or decode a string of lowercase letters with an alphanumeric cipher that contains uppercase letters and duplicates