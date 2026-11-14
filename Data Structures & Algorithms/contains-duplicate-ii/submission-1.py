class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap={}#empty dictionary that will store val:index
        n=len(nums)
        for i in range(n):
            if nums[i] in hashmap:
                val=abs(i-hashmap[nums[i]])
                if val<=k:
                    return True 
                else:
                    hashmap[nums[i]]=i
            else:
                hashmap[nums[i]]=i
        return False
        