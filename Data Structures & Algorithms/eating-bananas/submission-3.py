import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1. No need to sort piles anymore! Finding max element is enough.
        left = 1
        right = max(piles)
        
        # Initialize speed to the maximum possible answer
        speed = right
        
        while left <= right:
            mid = (left + right) // 2
            time_req = 0
            
            # 2. RUN THE FOR LOOP COMPLETELY FIRST
            for k in piles:
                time_req += math.ceil(k / mid)
            
            # 3. DECIDE ONLY AFTER CHECKING ALL PILES
            if time_req <= h:
                speed = mid          # Record this valid speed
                right = mid - 1      # Try to find a smaller valid speed
            else:
                left = mid + 1       # This speed is too slow, look higher
                
        return speed

                
        



                



        