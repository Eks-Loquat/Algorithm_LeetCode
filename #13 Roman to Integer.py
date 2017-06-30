import time


def romanToInt(s):
    RTI = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    length = len(s)
    i = 0
    num = []
    while i < length:
        num.append(RTI[s[i]])
        i += 1
    i = 0
    while i < length - 1:
        if num[i] < num[i + 1]:
            num[i] = -num[i]
        i += 1
    return sum(num)


if __name__ == '__main__':
    start = time.clock()
    s = 'MMMCMXCIX'
    print(romanToInt(s))
    end = time.clock()
    print(end - start)
