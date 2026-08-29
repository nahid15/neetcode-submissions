class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ans = nums[0]

        for i in nums:
            if count == 0:
                count += 1
                ans = i
            if i == nums[0]:
                count += 1
            else:
                count -= 1
        return ans