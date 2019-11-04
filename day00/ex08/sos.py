import sys

morse = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'
}


def printMorseChar(c):
    print(morse.get(c), end='')


i = 1
while i < len(sys.argv):
    for c in sys.argv[i]:
        if not c.isalnum() and not c.isspace():
            print("ERROR")
            sys.exit()
    sys.argv[i] = sys.argv[i].lower()
    i += 1
i = 1
j = 0
while i < len(sys.argv):
    for k in sys.argv[i]:
        if k == ' ':
            print(' / ', end='')
        else:
            printMorseChar(k)
        j += 1
        if j != len(sys.argv[i]):
            print(' ', end='')
    j = 0
    i += 1
    if i != len(sys.argv):
        print(' / ', end='')
if len(sys.argv) != 1:
    print()
