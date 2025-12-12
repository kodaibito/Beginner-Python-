def find_pair(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [nums[left], nums[right]]
        elif total < target:
            left += 1
        else:
            right -= 1
    return -1