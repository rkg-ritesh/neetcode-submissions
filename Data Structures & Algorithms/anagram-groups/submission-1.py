class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection = {}
        for st in strs:
            newString = "".join(sorted(st))
            if newString in collection:
                collection[newString].append(st)
            else:
                collection[newString] = [st]

        return list(collection.values()) # one liner
