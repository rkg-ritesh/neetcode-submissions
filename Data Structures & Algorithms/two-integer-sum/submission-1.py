class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums=[]
        for i in range(len(nums)):
            new_nums.append([nums[i],i])
        new_nums.sort()
        i,j=0,len(nums)-1
        while i<j:
            sum=new_nums[i][0]+new_nums[j][0]
            if target==sum:
                return sorted([new_nums[i][1],new_nums[j][1]])
            elif target>sum:
                i+=1
            else:
                j-=1
        return []