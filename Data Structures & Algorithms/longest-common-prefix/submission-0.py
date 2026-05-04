class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        for item in strs:
            newString=""
            i,j=0,0
            while i<len(result) and j<len(item):
                if result[i]==item[j]:
                    newString+=result[i]
                else:
                    break;
                i+=1
                j+=1
            if newString=="":
                return ""
            result=newString
        return result