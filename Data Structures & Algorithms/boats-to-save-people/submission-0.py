class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res=0
        people.sort()
        left=0
        right=len(people)-1
        while left<=right:
            total=people[left]+people[right]
            if total<=limit:
                res+=1
                left+=1
                right-=1
            else:
                res+=1
                right-=1
        return res



        