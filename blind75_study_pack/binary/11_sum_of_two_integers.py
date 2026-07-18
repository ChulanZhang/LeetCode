from typing import List, Optional, Dict, Set

# Sum of Two Integers - Medium
# 🔑 Key Points: Bit Manipulation - XOR for carry-less addition, AND and Shift for carry
#
# 🧠 Intuition & Breaking Points:
#   - Intuition & Pitfalls: 
#     To add two integers without using '+' or '-', we must simulate adder circuits at the binary level. Addition of two numbers can be split into: carry-less sum (which can be calculated using XOR) and the carry bits (which can be calculated using AND followed by a left shift of 1).
#   - Mathematical Derivation: 
#     For two integers a and b:
#     1. `a ^ b` calculates the carry-less sum (e.g., 1+1=0, 1+0=1).
#     2. `(a & b) << 1` calculates the carry bits (since only 1+1 creates a carry, which is shifted left by 1).
#     3. Repeat this process recursively/iteratively until the carry `b` becomes 0.
#     In Python, integers have arbitrary precision, so we must manually apply a 32-bit mask `0xFFFFFFFF` to simulate the overflow and negative bounds of a standard 32-bit signed integer.

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Time Complexity: O(1) - Loop runs at most 32 times for a 32-bit integer
        # Space Complexity: O(1)
        
        # Max positive 32-bit signed integer
        MAX = 0x7FFFFFFF
        # 32-bit mask to handle Python's arbitrary precision
        mask = 0xFFFFFFFF
        
        while b != 0:
            # Carry bits are computed by ANDing and shifting left by 1
            carry = (a & b) << 1
            # Carry-less sum is computed by XORing and masked to 32 bits
            a = (a ^ b) & mask
            # Update b to hold the carry bits for the next iteration
            b = carry & mask
            
        # If the result is negative (MSB is 1, i.e., > MAX), map it back to Python's negative representation
        return a if a <= MAX else ~(a ^ mask)

