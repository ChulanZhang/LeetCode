from typing import List, Optional, Dict, Set

# Reverse Bits - Easy
# 🔑 Key Points: Bit Manipulation - Shift and Accumulate
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     We can process the 32 bits of `n` one by one. In each step, we extract the LSB of `n` and shift it to its reversed position in the result.
#   - Mathematical Derivation: 
#     1. Initialize the result `res = 0`.
#     2. Loop 32 times:
#        - Shift the result left by 1 to make space: `res <<= 1`.
#        - Extract the LSB of `n` and bitwise OR it into the result: `res |= (n & 1)`.
#        - Shift `n` right by 1 to process the next bit: `n >>= 1`.
#     This correctly reverses all 32 bits and works for both signed and unsigned representations.

class Solution:
    def reverseBits(self, n: int) -> int:
        # Time Complexity: O(1) - Fixed 32 iterations
        # Space Complexity: O(1)
        res = 0
        for _ in range(32):
            # Shift result left and add the LSB of n
            res = (res << 1) | (n & 1)
            # Shift n right to prepare the next bit
            n >>= 1
        return res

