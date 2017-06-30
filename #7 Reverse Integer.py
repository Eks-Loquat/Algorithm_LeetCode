import time


def reverse(x):
    minus = 0
    if x < 0:
        minus = 1
        x = abs(x)
    s = str(x)
    length = len(s)
    i = 0
    s_new = ''
    while i < length:
        s_new = s_new + s[length - i - 1]
        i = i + 1
    x_new = int(s_new)
    if minus == 1:
        x_new = -x_new
    if -2147483648 <= x_new <= 2147483647:
        return x_new
    else:
        return 0


if __name__ == '__main__':
    start = time.clock()
    x = 2222222222222
    print(reverse(x))
    end = time.clock()
    print(end - start)
