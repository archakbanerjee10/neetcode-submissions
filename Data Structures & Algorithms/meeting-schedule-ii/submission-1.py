"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        st=sorted([i.start for i in intervals])
        en=sorted([i.end for i in intervals])
        i,j=0,0
        res,count=0,0
        while i <len(st):
            if st[i]<en[j]:
                count+=1
                i+=1
            else:
                count-=1
                j+=1
            res=max(res,count)

        return res 

        

        