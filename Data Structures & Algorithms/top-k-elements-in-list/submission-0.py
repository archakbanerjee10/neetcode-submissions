class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        hash_map={}
        result=[]
        fin=[]
        for i in range(n):
            if nums[i] in hash_map:
                hash_map[nums[i]]+=1
            else:
                hash_map[nums[i]]=1
        result=sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
        for key , value in result:
            if len(fin)==k:
                break
            else:
                fin.append(key)
                
        return fin

