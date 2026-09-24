class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for index, value in enumerate(nums):
            remaining = target - value
            if remaining in seen:
                return [seen[remaining], index]
            seen[value] = index

        return []