class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #disctionary based
        count = {}
        for i in nums:
            count[i] = count.get(i,0)+1

        return max(count.keys(), key=count.get)