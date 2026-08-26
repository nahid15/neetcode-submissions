class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = 0
        if len(nums) != 0 and len(nums)>1:
            for i in range(len(nums)):
                for j in range(i+1 , len(nums)):
                    if nums[i] != nums[j]:
                        flag = 1
                        continue
                    else:
                        flag =0
                        break
                if flag == 0:
                    break
        else:
            flag = 1
            
        return bool(flag==0)
