class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        for x,y in points :
            dis=(x**2)+(y**2)
            minHeap.append([dis,x,y])
        heapq.heapify(minHeap)
        result=[]
        for i in range(k):
            dis,x,y=heapq.heappop(minHeap)
            result.append([x,y])
        return result


        