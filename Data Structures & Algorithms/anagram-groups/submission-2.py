class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Automatically creates an empty list for new keys
        result = defaultdict(list) 
        
        for word in strs:
            count = [0] * 26
            for alpha in word:
                count[ord(alpha) - ord("a")] += 1

            result[tuple(count)].append(word)
            
        return list(result.values())
                

        