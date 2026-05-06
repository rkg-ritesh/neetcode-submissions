class Solution:
    def merge(self,nums: List[int], start: int, mid: int, end: int) -> None:
        n1 = mid - start + 1
        n2 = end - mid
        l1 = [0] * n1
        r1 = [0] * n2
        for i in range(n1):
            l1[i] = nums[i + start]
        for i in range(n2):
            r1[i] = nums[mid + 1 + i]
        i, j, k = 0, 0, start

        while i < n1 and j < n2:
            if l1[i] <= r1[j]:
                nums[k] = l1[i]
                i+=1
            else:
                nums[k] = r1[j]
                j+=1
            k += 1
        while i < n1:
            nums[k] = l1[i]
            i += 1
            k += 1
        while j < n2:
            nums[k] = r1[j]
            j += 1
            k += 1

    def mergeSort(self, nums: List[int], start: int, end: int) -> None:
        if start >= end:
            return
        mid = start + (end - start) // 2
        self.mergeSort(nums, start, mid)
        self.mergeSort(nums, mid + 1, end)
        self.merge(nums, start, mid, end)

    def sortArray(self, nums: List[int]) -> List[int]:
        """
        lets try to implement the merge sort
        """
        start, end = 0, len(nums) - 1
        self.mergeSort(nums, start, end)
        return nums
