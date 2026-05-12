class Solution:
    def reverse(self,i:int,j:int,nums:List[int])->None:
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        self.reverse(0,len(nums)-1-k,nums)
        self.reverse(len(nums)-k,len(nums)-1,nums)
        self.reverse(0,len(nums)-1,nums)


        