class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap={}
        #store last occurences of the alpabet in the hashmap 
        for i in range(len(s)-1,-1,-1):
            if s[i] in hashmap:
                continue
            else:
                hashmap[s[i]]=i

        #this is our list which we will return 
        output=[]
        size,end=0,0
        for i,c in enumerate(s):
            size+=1
            end=max(end,hashmap[c])

            if i==end:
                output.append(size)
                size=0
        return output
        


        