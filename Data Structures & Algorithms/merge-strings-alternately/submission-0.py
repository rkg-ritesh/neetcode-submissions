class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length=len(word1)+len(word2)
        ans=[""]*(length)
        i=0
        j=0
        k=0
        while i<len(word1) and j<len(word2):
            if k%2==0:
                ans[k]=word1[i]
                k+=1
                i+=1
            else:
                ans[k]=word2[j]
                k+=1
                j+=1
        while i<len(word1):
            ans[k]=word1[i]
            k+=1
            i+=1
        while j<len(word2):
            ans[k]=word2[j]
            k+=1
            j+=1
        ans="".join(ans)
        return ans

