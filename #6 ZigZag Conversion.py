import time


def convert(s, numRows):
    if numRows == 1:
        return s
    i = 0
    length = len(s)
    tmp_str = ''
    s_new = ''
    while i < numRows and i < length:
        rowNum = i
        if i == 0 or i == numRows - 1:
            tmp_str = tmp_str + s[i]
            while i + numRows * 2 - 2 < length:
                i = i + numRows * 2 - 2
                tmp_str = tmp_str + s[i]
        else:
            tmp_str = tmp_str + s[i]
            while i + numRows * 2 - 2 * rowNum - 2 < length:
                i = i + numRows * 2 - 2 * rowNum - 2
                tmp_str = tmp_str + s[i]
                if i + 2 * rowNum < length:
                    i = i + 2 * rowNum
                    tmp_str = tmp_str + s[i]
                else:
                    break
        s_new = s_new + tmp_str
        tmp_str = ''
        i = rowNum + 1
    return s_new


if __name__ == '__main__':
    start = time.clock()
    s = 'PAYPALISHIRING'
    numRows = 4
    print(convert(s, numRows))
    end = time.clock()
    print(end - start)
