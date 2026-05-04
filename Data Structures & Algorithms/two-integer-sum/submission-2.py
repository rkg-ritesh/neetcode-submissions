class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,val in enumerate(nums):
            complement=target-val
            if complement in seen:
                return sorted([i,seen[complement]])
            seen[val]=i
        return []