class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first=0
        second=0
        res=""
        while first<len(word1) and second<len(word2):
            res+=word1[first]
            first+=1
            res+=word2[second]
            second+=1
        
        while first<len(word1):
            res+=word1[first]
            first+=1
        
        while second<len(word2):
            res+=word2[second]
            second+=1
        return res

        