class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            #print(nums[i])
            need = target-nums[i]
            nums[i]='*'
            #print(need)
            if need in nums:
                return [i, nums.index(need)]