def check_validity(cipher: str) -> bool:
    if len(cipher) == len(set(cipher)) and len(cipher) == 26:
        return True
    return False

def encode_text(cipher: str) -> dict:
    return {cipher[i]: cipher[0] if i == len(cipher)-1 else cipher[i+1] for i in range(len(cipher)-1)}

def generate_encrypted_text(text: str, dictionary: dict) -> str:
    return "".join([dictionary[char] for char in text])

def get_key(code: str, dictionary: dict) -> str:
    for encryption, char in dictionary.items():
        if code == char:
            return encryption


def decode_text(dictionary: dict, text: str):
    new_text = ""
    for char in text:
        addition = get_key(char, dictionary)
        new_text = new_text + addition
    return new_text


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
            cipher = input("Please enter cipher text: ")
            if check_validity(cipher):
                break
            print("Your cipher must contain 26 unique elements of a-z or 0-9\n")
        dictionary = encode_text(cipher)
        encrypted_text = generate_encrypted_text(text, dictionary)
        print("Your output is: ", encrypted_text, "\n")
    if user_input == 2:
        text_to_decode = input("Please enter the text to be processed: ")
        while True:
            cipher = input("Please enter cipher text: ")
            if check_validity(cipher):
                break
            print("Your cipher must contain 26 unique elements of a-z or 0-9\n")
        decoded_text = decode_text(dictionary, text_to_decode)
        print("Your output is: ", decode_text, "\n")
        



#bcdefghijklmnopqrstuvwxyza