class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            gap = target - nums[i]
            if gap not in h:
                h[nums[i]] = i
            else:
                return [h[gap], i]
            
            
