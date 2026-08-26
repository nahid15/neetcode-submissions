class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}

        for i, n in enumerate(nums):
            need = target - n
            if need in hMap:
                return [hMap[need], i]
            hMap[n] = i