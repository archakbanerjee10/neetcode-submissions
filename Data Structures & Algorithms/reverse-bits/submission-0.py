class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
        # Extract the rightmost bit of n and shift it to its reversed position
            result = (result << 1) | (n & 1)
        # Shift n right to process the next bit
            n >>= 1
        return result
        