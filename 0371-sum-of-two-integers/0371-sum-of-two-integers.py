class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        a &= MASK
        b &= MASK

        while b != 0:
            current_sum = (a ^ b) & MASK
            carry = ((a & b) << 1) & MASK
            
            a = current_sum
            b = carry
        
        if a <= MAX_INT:
            return a
        return ~(a ^ MASK)

        