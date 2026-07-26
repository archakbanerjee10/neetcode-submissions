class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        new_num = abs(x)
        
        # Reverse the digits
        while new_num:
            dg = new_num % 10
            result = result * 10 + dg
            new_num //= 10
        
        # Reapply the negative sign if original x was negative
        if x < 0:
            result *= -1
            
        # Check 32-bit signed integer bounds
        if result < -2**31 or result > 2**31 - 1:
            return 0
            
        return result
            



        