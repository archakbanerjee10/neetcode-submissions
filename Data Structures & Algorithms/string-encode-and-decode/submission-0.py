class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString=""
        for word in strs:
            encodedString+=str(len(word))+"#"
            encodedString+=word
        return encodedString


    def decode(self, s: str) -> List[str]:
        j=0
        i=1
        result=[]
        while i< (len(s)):
            if(s[i]=="#"):
                word=""
                num=int(s[j:i])
                k=i+1
                rang=k+num
                while k < rang:
                    word+=s[k]
                    k+=1
                result.append(word)
                j=k
                i=k
            else:
                i+=1
        return result
            
                
            



               
