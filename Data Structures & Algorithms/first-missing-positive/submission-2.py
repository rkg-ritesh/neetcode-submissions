class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        eleSet=set(nums)
        
        for i in range(1,max(eleSet)+2):
            if i not in eleSet:
                return i
        return 1
