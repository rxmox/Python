char_count = 0
user_text = ('Alo A!Xel,')
for character in user_text:
    if (character != ' ') or (character != '.') or (character != ',') or (character != '!'):
        char_count +=1

print(char_count)
