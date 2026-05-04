class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result =strs[0]
        for i in range(len(result)):
            char=result[i]
            for j in range(1,len(strs)):
                if i==len(strs[j]) or strs[j][i]!=char:
                    return result[:i]
        return result