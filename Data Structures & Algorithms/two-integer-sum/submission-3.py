class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        for i in range(len(nums)):
        #num= nums[i]
            need = target-nums[i]
            #print(i, nums[i],'-', need)
            if need in seen_map:
                return [seen_map[need], i]

            seen_map[nums[i]]=i
            #print(seen_map)