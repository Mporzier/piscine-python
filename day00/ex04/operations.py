import sys

if (len(sys.argv) != 3):
    if (len(sys.argv) > 3):
        print("InputError: too many arguments")
    print("Usage: python operations.py")
    print("Example:")
    print("    python operations.py 10 3")
    sys.exit()
test1 = sys.argv[1].replace('-', '', 1)
test2 = sys.argv[2].replace('-', '', 1)
if (not test1.isdigit()) or (not test2.isdigit()):
    print("InputError: only numbers")
    print("Usage: python operations.py")
    print("Example:")
    print("    python operations.py 10 3")
    sys.exit()
first = int(sys.argv[1])
second = int(sys.argv[2])
print("Sum:         ", first + second)
print("Difference:  ", first - second)
print("Product:     ", first * second)
print("Quotient:     ", end='')
if second == 0:
    print("ERROR (div by zero)")
else:
    print(first / second)
print("Remainder:    ", end='')
if second == 0:
    print("ERROR (modulo by zero)")
else:
    print(first % second)
