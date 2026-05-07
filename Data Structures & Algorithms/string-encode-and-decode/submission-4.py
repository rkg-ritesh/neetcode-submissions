class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(str)}#{str}" for str in strs)

    def decode(self, s: str) -> List[str]:
        """
        this was the tought part because first we need to find the '#' 
        then the left will be the count and the right will be the string 
        """
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

