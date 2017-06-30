def twoSum(nums, target):
    tmp_num = {}
    for i in range(len(nums)):
        if target - nums[i] in tmp_num:
            return [tmp_num[target - nums[i]], i]
        else:
            tmp_num[nums[i]] = i
    return [-1, -1]

if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    target = 6
    ans = twoSum(nums, target)
    print(ans)
