class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        i = 0
        while i < len(nums) - 3:
            j = i + 1
            while j < len(nums) - 2:
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        lastk = nums[k]
                        while k < len(nums) and lastk == nums[k]:
                            k += 1
                        lastl = nums[l]
                        while l >= 0 and lastl == nums[l]:
                            l -= 1
                    elif sum > target:
                        l -= 1
                    else:
                        k += 1
                lastj = nums[j]
                while j < len(nums) and lastj == nums[j]:
                    j += 1
            lasti = nums[i]
            while i < len(nums) and lasti == nums[i]:
                i += 1
        return ans
