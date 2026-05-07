class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixMul=list(nums)
        suffixMul=list(nums)  
        for i in range(1,len(nums)):
            prefixMul[i]*=prefixMul[i-1]       
        for i in range(len(nums)-2,-1,-1):
            suffixMul[i]*=suffixMul[i+1]
        
        ans=[]
        for i in range(len(nums)):
            left,right=1,1
            if i!=0:
                left=prefixMul[i-1]
            if i!=len(nums)-1:
                right=suffixMul[i+1]
            ans.append(left*right)
        return ans


