class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        collection = {}
        for st in strs:
            newString = "".join(sorted(st))
            if newString in collection:
                collection[newString].append(st)
            else:
                collection[newString] = [st]

        ans = []
        for val in collection.values():
            ans.append(val)

        return ans
