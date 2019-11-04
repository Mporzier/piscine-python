import sys
import string
import re

if (len(sys.argv) != 3) or (not sys.argv[2].isdigit()) or (sys.argv[1].isdigit()):
    print("ERROR")
    sys.exit()
words = re.split(r'\s+|[,;.-]\s*', sys.argv[1])
length = int(sys.argv[2])
i = 0
while i < len(words):
    if len(words[i]) <= length:
        words.remove(words[i])
        i = -1
    i += 1
print(words)
