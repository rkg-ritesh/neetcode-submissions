from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        countEle=Counter(nums)
        ans=[]
        for key,value in countEle.items():
            if value> len(nums)//3:
                ans.append(key)
        return ans
        