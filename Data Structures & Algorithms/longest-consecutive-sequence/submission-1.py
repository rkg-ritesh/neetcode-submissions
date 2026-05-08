class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        count=[1]*len(nums)
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                count[i]=count[i-1]+1
            elif nums[i]==nums[i-1]:
                count[i]=count[i-1]

        return max(count)
            
        
                
        
