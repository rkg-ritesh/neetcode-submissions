class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i=0
        ans=[]
        while i< len(nums):
            target=-1*nums[i]
            j,k=i+1,len(nums)-1
            while j<k:
                sum=nums[j]+nums[k]
                if sum==target:
                    ans.append([nums[i],nums[j],nums[k]])
                    lastj=nums[j]
                    while j<len(nums) and nums[j]==lastj:
                        j+=1
                    lastk=nums[k]
                    while k>=0 and nums[k]==lastk:
                        k-=1
                elif sum>target:
                    k-=1
                else:
                    j+=1
            last=nums[i]
            while i<len(nums) and nums[i]==last:
                i+=1
        return ans