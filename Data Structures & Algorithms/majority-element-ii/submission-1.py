class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1,cand2,count1,count2=None,None,0,0
        for ele in nums:
            if ele==cand1:
                count1+=1
            elif ele==cand2:
                count2+=1
            elif count1==0:
                cand1,count1=ele,1
            elif count2==0:
                cand2,count2=ele,1
            else:
                count1-=1
                count2-=1
        ans=[]
        for ele in [cand1,cand2]:
            if nums.count(ele)>len(nums)//3:
                ans.append(ele)
        return ans

        