class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        my_dict={}
        for char in s1:
            if char not in my_dict:
                my_dict[char]=1
            else:
                my_dict[char]+=1
        length=len(s1)
        left=0
        my_dict2={}
        for right in range(len(s2)):
            if(right-left+1>length):
                my_dict2[s2[left]]-=1
                if(my_dict2[s2[left]]==0):
                    del my_dict2[s2[left]]
                left+=1
                
            my_dict2[s2[right]] = my_dict2.get(s2[right], 0) + 1
            if(my_dict==my_dict2):
                return True
        return False
                