import time


def intToRoman(num):
    digit_1 = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
    digit_2 = {0: '', 1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
    digit_3 = {0: '', 1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
    digit_4 = {0: '', 1: 'M', 2: 'MM', 3: 'MMM'}
    d_4 = int(num / 1000)
    num = num - d_4 * 1000
    d_3 = int(num / 100)
    num = num - d_3 * 100
    d_2 = int(num / 10)
    num = num - d_2 * 10
    d_1 = num
    roman = digit_4[d_4] + digit_3[d_3] + digit_2[d_2] + digit_1[d_1]
    return roman


if __name__ == '__main__':
    start = time.clock()
    num = 3999
    print(intToRoman(num))
    end = time.clock()
    print(end - start)
