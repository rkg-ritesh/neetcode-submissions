class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection={}

        for item in strs:
            count=[0]*26
            for char in item:
                count[ord(char)-ord('a')]+=1
            t=tuple(count)
            if t in collection:
                collection[t].append(item)
            else:
                collection[t]=[item]
        
        return list(collection.values())
