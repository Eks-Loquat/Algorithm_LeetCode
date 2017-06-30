import time


def findMedianSortedArrays(nums1, nums2):
    length1 = len(nums1)
    length2 = len(nums2)
    i = 0
    j = 0
    nums = []
    while i < length1 and j < length2:
        if (nums1[i] >= nums2[j]):
            nums.append(nums2[j])
            j += 1
        else:
            nums.append(nums1[i])
            i += 1

    if i == length1:
        nums = nums + nums2[j:]
    if j == length2:
        nums = nums + nums1[i:]
    print(nums)
    if len(nums) % 2 == 0:
        return (nums[int(len(nums) / 2)] + nums[int(len(nums) / 2) - 1]) / 2
    else:
        return nums[int(len(nums) / 2)]


if __name__ == '__main__':
    start = time.clock()
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(findMedianSortedArrays(nums1, nums2))
    end = time.clock()
    print(end - start)
