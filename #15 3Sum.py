import time


def threeSum(nums):
    if len(nums) < 3:
        return []
    nums = sorted(nums)
    i = 0
    threeAns = []
    while i < len(nums):
        two_nums = nums[i + 1:]
        two_ans = twoSum(two_nums, -nums[i])
        if len(two_ans) > 0:
            j = 0
            while j < len(two_ans):
                threeAns.append([nums[i], two_ans[j][0], two_ans[j][1]])
                j += 1
        i += 1

    i = 0
    ans = []
    while i < len(threeAns):
        if sorted(threeAns[i]) not in ans:
            ans.append(sorted(threeAns[i]))
        i += 1
    return ans


def twoSum(nums, target):
    twoAns = []
    while 1 < len(nums):
        res = nums[0]
        nums = nums[1:]
        if target - res in nums:
            if [res, target - res] not in twoAns:
                twoAns.append([res, target - res])
    return twoAns


# def twoSum(nums, target):
#     i = 0
#     j = len(nums) - 1
#     twoAns = []
#     while i < j:
#         if nums[i] + nums[j] == target:
#             if [nums[i], nums[j]] not in twoAns:
#                 twoAns.append([nums[i], nums[j]])
#             j -= 1
#         if nums[i] + nums[j] > target:
#             j -= 1
#             continue
#         if nums[i] + nums[j] < target:
#             i += 1
#             continue
#     return twoAns


if __name__ == '__main__':
    start = time.clock()
    S = [-1,0,1,-1,2,-4]
    print(threeSum(S))
    end = time.clock()
    print(end - start)
