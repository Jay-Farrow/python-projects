# Text to Morse Code Converter
# Programmer: Jason Farrow
# Date: 06/05/2024

morse_code_alphabet = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
}

string_to_convert = input("Enter a text string to convert to Morse Code: ").upper()

morse_code_result = ''
for letter in string_to_convert:
    if letter == ' ':
        morse_code_result += '/ '
    else:
        morse_code_result += morse_code_alphabet[letter]
        morse_code_result += ' '

print(morse_code_result)
