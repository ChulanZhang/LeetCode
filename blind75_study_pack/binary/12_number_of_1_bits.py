from typing import List, Optional, Dict, Set

# Number of 1 Bits - Easy
# 🔑 Key Points: Bit Manipulation - Brian Kernighan's Algorithm (n & (n - 1))
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     The standard solution checks the least significant bit (LSB) and shifts right 32 times. However, this always takes 32 iterations, even if the number contains only a single 1 bit.
#   - Mathematical Derivation: 
#     Brian Kernighan's algorithm optimizes this by clearing the lowest set bit using `n & (n - 1)`. For any number `n`, `n - 1` flips all bits to the right of the lowest set bit (including the set bit itself). Thus, `n & (n - 1)` clears the lowest set bit while keeping all higher bits unchanged. This means the number of iterations equals exactly the number of set bits, which is extremely efficient.

class Solution:
    def hammingWeight(self, n: int) -> int:
        # Time Complexity: O(1) - Iterations match the number of set bits (maximum 32)
        # Space Complexity: O(1)
        count = 0
        while n:
            # Clear the lowest set bit of n
            n = n & (n - 1)
            count += 1
        return count

