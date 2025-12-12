def find_triplet(nums, target):
    for i in range(len(nums)):
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == target:
                return [nums[i], nums[left], nums[right]]
            elif total < target:
                left += 1
            else:
                right -= 1
    return -1