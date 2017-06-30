import time


def isPalindrome(x):
    s = str(x)
    length = len(s)
    i = 0
    while i < int(length / 2):
        if s[i] == s[length - 1 - i]:
            i = i + 1
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    start = time.clock()
    x = 1234321
    print(isPalindrome(x))
    end = time.clock()
    print(end - start)
