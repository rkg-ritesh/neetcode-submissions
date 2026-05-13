class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i,j=0,len(people)-1
        ans=0
        while i<j:
            sum=people[i]+people[j]
            if sum<=limit:
                i+=1
                j-=1
            elif sum>limit:
                j-=1
            ans+=1
        if i==j:
            ans+=1
        return ans
                
            