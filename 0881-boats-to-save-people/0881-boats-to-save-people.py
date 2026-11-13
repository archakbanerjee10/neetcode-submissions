class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        res=0
        left=0
        right=len(people)-1
        while left<=right:
            total=people[left]+people[right]
            if total<=limit:
                left+=1
                right-=1
                res+=1
            else:
                res+=1
                right-=1
        return res
        