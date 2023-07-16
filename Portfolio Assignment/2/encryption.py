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
    """
    Checks that the length of cipher is 26 and that all characters are alphanumeric  

    Arguments:
    cipher -- string representing the cipher that has been entered by the user

    Returns:
    Returns True if the cipher entered by the user is valid, meaning that it has 26 characters that are all alphanumeric
    Returns False if the cipher entered by the user is invalid

    """

def encode(text,cipher_value):
    dict1= {'a' : cipher_value[0],'b' : cipher_value[1],'c' : cipher_value[2],'d' : cipher_value[3],'e' : cipher_value[4],'f' : cipher_value[5],'g' : cipher_value[6],'h' : cipher_value[7],'i' : cipher_value[8],'j' : cipher_value[9],'k' : cipher_value[10],'l' : cipher_value[11],'m' : cipher_value[12],'n' : cipher_value[13],'o' : cipher_value[14],'p' : cipher_value[15],'q' : cipher_value[16],'r' : cipher_value[17],'s' : cipher_value[18],'t' : cipher_value[19],'u' : cipher_value[20],'v' : cipher_value[21],'w' : cipher_value[22],'x' : cipher_value[23],'y' : cipher_value[24],'z' : cipher_value[25],}
    n=0
    encryption = []
    for i in range(len(text)):
        encryption.append(dict1[text[n]])
        n+=1
    return''.join(encryption)
    """
    Creates a list for encryption from the dictionary

    Arguments:
    text -- string representing the text entered by the user that will then be encoded
    cipher_value -- the cipher entered by the user which will be used as values for the keys in the dictionary

    Returns:
    Returns a list of all the values in encryption joined together in a string

    """

def decode(text,decipher_value):
    dict2 = {decipher_value[0]: 'a',decipher_value[1]: 'b',decipher_value[2]: 'c',decipher_value[3]: 'd',decipher_value[4]: 'e',decipher_value[5]: 'f',decipher_value[6]: 'g',decipher_value[7]: 'h',decipher_value[8]: 'i',decipher_value[9]: 'j',decipher_value[10]: 'k',decipher_value[11]: 'l',decipher_value[12]: 'm',decipher_value[13]: 'n',decipher_value[14]: 'o',decipher_value[15]: 'p',decipher_value[16]: 'q',decipher_value[17]: 'r',decipher_value[18]: 's',decipher_value[19]: 't',decipher_value[20]: 'u',decipher_value[21]: 'v',decipher_value[22]: 'w',decipher_value[23]: 'x',decipher_value[24]: 'y',decipher_value[25]: 'z',}
    n=0
    decryption = []
    for i in range(len(text)):
        decryption.append(dict2[text[n]])
        n+=1
    return''.join(decryption)
    """
    Creates a list for decryption from the dictionary

    Arguments:
    text -- string representing the text entered by the user that will then be decoded
    decipher_value -- the cipher entered by the user which will be used as keys for the values in the dictionary

    Returns:
    Returns a list of all the values in decryption joined together in a string

    """


print("ENDG 233 Encryption Program")

### Add your main program code here

# Text asking for user input
intro_text = ("What would you like to do?\n"
             "1: Encode text\n"
             "2: Decode text\n"
             "0: End the program\n"
             "Input: ")

# Continuous input loop             
while True:
    user_input = int(input(intro_text))
    if user_input == 0:                                            # Ends the program if the user enters 0
        break
    if user_input == 1:                                              # Takes inputs for encoding if user enters 1
        text = input("Please enter the text to be processed: ")
        while True:                                                  # Continuous input loop checking that the user enters a valid cipher
            cipher = input("Please enter cipher text: ").lower()     # Bonus: converting user input to lowercase
            unique_cipher = []                                       
            for i in cipher:                                         # removes any duplicates in cipher
                if i not in unique_cipher:
                    unique_cipher.append(i)
            cipher = ''.join(unique_cipher)
            if check_validity(cipher):                               # call the check_validity function
                break
            print("Your cipher must contain 26 unique elements of a-z or 0-9\n")  
        print('Your cipher is valid.')
        encoded_message= encode(text,cipher)
        print("Your output is: ", encoded_message, "\n")                # printing out encoded message to user


    if user_input == 2:                                                 # Takes input for decoding if user enters 2
        text = input("Please enter the text to be processed: ")         
        while True:                                                     # Continuous input loop checking that the user enters a valid cipher
            decipher = input("Please enter cipher text: ").lower()      # Bonus: converting user input to lowercase
            unique_decipher = []                                      
            for i in decipher:                                          # removes any duplicates in cipher
                if i not in unique_decipher:
                    unique_decipher.append(i)
            decipher = ''.join(unique_decipher)
            if check_validity(decipher):                                # call the check_validity function
                break
            print("Your cipher must contain 26 unique elements of a-z or 0-9\n")
        print('Your cipher is valid.')
        decoded_message= decode(text,decipher)
        print("Your output is: ", decoded_message, "\n")                # printing out encoded message to user
        
print('Thank you for using the encryption program.')
