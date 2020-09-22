alphabet = ''.join([chr(num) for num in range(97, 123)])

while True:
    try:
        filename = input('Enter a filename: ')
        with open(filename, 'r') as f:
            content = f.read()
    except Exception as err:
        print(err)
    else:
        break

while True:
    try:
        key = int(input('Key that you want to apply for the cipher: '))
        if key not in range(1, 25):
            raise Exception(f'Invalid key. Keys must be between 1-25')
    except (TypeError, ValueError):
        print('Invalid value.')
    except Exception as err:
        print(err)
    else:
        break

encrypted = ''
with open(filename, 'r') as f:
    for line in f.readlines():
        for character in line:
            if character in alphabet:
                index = (alphabet.index(character) + key) % 26
                encrypted += alphabet[index]
            elif character in alphabet.upper():
                index = (alphabet.upper().index(character) + key) % 26
                encrypted += alphabet.upper()[index]
            else:
                encrypted += character

with open('zen_python.txt', 'w') as f:
    f.write(encrypted)
