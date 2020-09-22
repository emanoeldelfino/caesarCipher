import string

alphabet = string.ascii_lowercase

letters_count = {}

filename = input('Enter a filename: ')

with open(filename) as f:
    text = f.read()

char_perc = [(char, round(100 * text.lower().count(char) / len(text), 2)) for char in alphabet]

char_perc.sort(key=lambda elem: elem[1], reverse=True)

# for key, value in char_perc:
#     print(f'{key} -> {value}%')

letter = char_perc[0][0]

# as 'E' is the most common letter in English it is used as reference to get the most
# common key in the ciphered text and get the key to solve that.
e_index = alphabet.index('e')
letter_index = alphabet.index(letter)

# get the key to solve the ceaser cipher
key = e_index - letter_index if e_index < letter_index else letter_index - e_index

decrypted = ''
for char in text:
    if char in alphabet:
        index = (alphabet.index(char) + key) % 26
        decrypted += alphabet[index]
    elif char in alphabet.upper():
        index = (alphabet.upper().index(char) + key) % 26
        decrypted += alphabet.upper()[index]
    else:
        decrypted += char

with open(filename, 'w') as f:
    f.write(decrypted)
