import time


def myAtoi(str):
    if str == "":
        return None
    length = len(str)
    i = 0
    while i < length:
        if '0' <= str[i] <= '9':
            i = i + 1
            continue
        return None
    return int(str)


if __name__ == '__main__':
    start = time.clock()
    str = '123+'
    print(myAtoi(str))
    end = time.clock()
    print(end - start)
