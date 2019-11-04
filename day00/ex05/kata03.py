import sys

i = 0
phrase = "The right format"
while i + len(phrase) < 42:
    print('-', end='')
    i += 1
print(phrase, end='')
