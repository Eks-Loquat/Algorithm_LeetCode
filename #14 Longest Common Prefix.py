import time


def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    prefix = strs[0]
    i = 1
    while i < len(strs):
        min_l = min(len(strs[i]), len(prefix))
        if min_l == len(strs[i]):
            prefix=prefix[:min_l]
        j = 0
        while j < min_l:
            if prefix[j] == strs[i][j]:
                j += 1
                continue
            prefix = prefix[:j]
            break
        i += 1
    return prefix


if __name__ == '__main__':
    start = time.clock()
    strs = ['aaabb', 'aaacc', 'aaadd']
    print(longestCommonPrefix(strs))
    end = time.clock()
    print(end - start)
