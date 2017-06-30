import time


def maxArea(height):
    length = len(height)
    i = 0
    j = length - 1
    mArea = 0
    while i < j:
        tmpWidth = j - i
        tmpHeight = min(height[i], height[j])
        tmpArea = tmpWidth * tmpHeight
        if tmpArea > mArea:
            mArea = tmpArea
        if height[i] == tmpHeight:
            i += 1
        else:
            j -= 1
    return mArea


if __name__ == '__main__':
    start = time.clock()
    height = [1, 2]
    print(maxArea(height))
    end = time.clock()
    print(end - start)
