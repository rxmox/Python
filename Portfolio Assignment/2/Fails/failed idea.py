#Creating our Standard Dictionary
main_list = "".join([chr(letter) for letter in range(97,123)] + [str(i) for i in range(10)])
shuffled_main_list = "jiqco04knm9depb67wasx5v81g3zutlhy2rf"

standard_dictionary = dict(zip(main_list,shuffled_main_list))

print(standard_dictionary)

#Function for creating the cipher dictionary
def create_cipher_dictionary(cipher):
    return {char: standard_dictionary[char] for char in cipher}
    """
    cipher_dictionary = {}
    for char in cipher:
        cipher_dictionary[char] = standard_dictionary[char]
    return cipher_dictionary
    """
text = "tellmeandiforgetteachmeandirememberinvolvemeandilearnbenjaminfranklin24753"
cipher = "bcd5fghijk60nopq1stu43xy2a"

cipher_dictionary = create_cipher_dictionary(cipher)
print(cipher_dictionary)


# #----Creating an ordered set
# new_text = []
# for i in list(text):
#     if i not in new_text:
#         new_text.append(i)
# new_text = "".join(new_text)

# new_text = ""
# for i in list(text):
#     new_text = new_text + i if i not in new_text else new_text

# print(new_text)


# #----Creating the dictionary
# dictionary = dict(zip(new_text,cipher))


# print(dictionary)


# #Generating encoded text
# encoded_text = "".join([dictionary[char] for char in new_text])
# print(encoded_text)
