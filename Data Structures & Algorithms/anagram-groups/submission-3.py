from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection=defaultdict(list)

        for item in strs:
            count=[0]*26
            for char in item:
                count[ord(char)-ord('a')]+=1
            collection[tuple(count)].append(item)
        
        return list(collection.values())
