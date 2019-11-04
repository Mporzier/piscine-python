import sys
import time


def ft_progress(listy):
    length = len(listy)

    def show(i):
        x = int(30 * i / length)
        sys.stdout.write("%s: %.2fs [ %d%s][%s%s%s] %i/%i\r" %
                         ("ETA", ((length - i) * 0.01), (100 * i / length), '%', "="*x, '>', " "*(30-x), i, length))
        sys.stdout.flush()

    for i, item in enumerate(listy):
        yield item
        show(i + 1)
    sys.stdout.write("\n")
    sys.stdout.flush()


listy = range(300)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
