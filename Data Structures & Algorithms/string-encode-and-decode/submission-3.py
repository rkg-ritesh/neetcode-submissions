class Solution:

    def encode(self, strs: List[str]) -> str:
        newStrs=[]
        # len#string
        for ele in strs:
            newStrs.append(str(len(ele)))
            newStrs.append('#')
            newStrs.append(ele)
        return "".join(newStrs)

    def decode(self, s: str) -> List[str]:
        i=0
        ans=[]
        while i<len(s):
            j=0
            while i+j<len(s) and s[i+j]!='#':
                j+=1
            length=int(s[i:i+j])
            string=s[i+j+1:i+j+1+length]
            i+=j+1+length
            ans.append(string)
        return ans

