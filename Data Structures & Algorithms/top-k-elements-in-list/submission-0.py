from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1
        sortedFreqArray=[]
        for keys,val in freq.items():
            sortedFreqArray.append([val,keys])
        sortedFreqArray.sort(reverse=True)

        ans=[]
        for num in sortedFreqArray[:k]:
            ans.append(num[1])
        return ans


        