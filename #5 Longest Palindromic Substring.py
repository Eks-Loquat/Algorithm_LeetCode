import time


def longestPalindrome(s):
    length = len(s)
    i = 0
    s_new = ''
    while i < length:
        s_new += '#'
        s_new += s[i]
        i += 1
    s_new += '#'
    print(s_new)
    length = len(s_new)
    print(length)
    max_str = s[0]
    tmp_len = 1
    max_len = 1
    i = 1
    while i < length - 1:
        j = 1
        while i - j >= 0 and i + j < length:
            if s_new[i - j] == s_new[i + j]:
                tmp_len += 2
                tmp_str = s_new[i - j:i + j + 1]
                j += 1
                if tmp_len > max_len:
                    max_len = tmp_len
                    max_str = tmp_str
            else:
                break
        tmp_len = 1
        i += 1
    print(max_str, max_len)
    if max_str[0] == '#':
        max_str = max_str[1::2]
        max_len = (max_len - 1) / 2
    else:
        max_str = max_str[::2]
        max_len = (max_len + 1) / 2
    return max_len, max_str


if __name__ == '__main__':
    start = time.clock()
    s = "aa"
    print(longestPalindrome(s))
    end = time.clock()
    print(end - start)
