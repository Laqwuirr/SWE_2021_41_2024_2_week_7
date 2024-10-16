from typing  import List

def twoSum(nums: List[int], target: int) -> List[int]:
    nums2 = nums[1:]
    for i in nums:
        for j in nums2:
            if i + j == target:
                return [nums.index(i), nums2.index(j) + 1]
            
nums = [3, 2, 4]
target = 7
print(twoSum(nums, target))
