import sys
string = ''
i = 0
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        if i:
            string += " "
        string += arg
        i += 1
string = string[::-1]
string = string.swapcase()
if string:
    print(string)
