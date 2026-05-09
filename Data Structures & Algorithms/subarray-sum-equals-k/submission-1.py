from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        """
        we are just focusing on the 
        prefixSum[j]-prefixSum[i]=k
                        
        ---------------------
        |_______|       
          pfS[i]         
        
        |____________________|
                pfS[j] 
                
                 |___________|
                   ans Subarray

        """
        prefixSum=defaultdict(int)
        prefix=0
        prefixSum[prefix]+=1
        ans=0
        for i,ele in enumerate(nums):
            nums[i]+=prefix
            if nums[i]-k in prefixSum:
                ans+=prefixSum[nums[i]-k]
            prefix=nums[i]
            prefixSum[prefix]+=1
        return ans


        