class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr=[-num for num in nums]
        minHeap=arr
        heapq.heapify(minHeap)
        i=0
        res=0
        while i<k:
            res=heapq.heappop(minHeap)
            i+=1 
        return -res if k<=len(nums) else 0
