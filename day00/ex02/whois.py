import sys

if len(sys.argv) == 1:
    sys.exit()
if (len(sys.argv) != 2) or (not sys.argv[1].lstrip('-').isdigit()):
    print("ERROR")
else:
    number = int(sys.argv[1])
    if number == 0:
        print("I'm Zero.")
    elif number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
