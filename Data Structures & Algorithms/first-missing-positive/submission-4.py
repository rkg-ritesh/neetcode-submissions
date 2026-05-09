class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        """
        so in here basicaaly we just try to put the element to their place ,
        only the element 1,n because only they matter nothing else
        1 go to nums[0] and similarly 
        and in the other loop we just see if i+1 is not present in i 
        
        """
        n=len(nums)
        i=0
        while i <n:
            if nums[i]>=1 and nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                targetPlace=nums[i]-1
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
            else:
                i+=1
        i=0
        while i <n:
            if nums[i]!=i+1:
                return i+1
            i+=1
        return n+1
        

