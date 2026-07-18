# Binary category data
PROBLEMS = {
    "11_sum_of_two_integers.py": {
        "title": "Sum of Two Integers",
        "difficulty": "Medium",
        "key_points": "Bit Manipulation - XOR for carry-less addition, AND and Shift for carry",
        "analysis_intuition": "To add two integers without using '+' or '-', we must simulate adder circuits at the binary level. Addition of two numbers can be split into: carry-less sum (which can be calculated using XOR) and the carry bits (which can be calculated using AND followed by a left shift of 1).",
        "analysis_derivation": "For two integers a and b:\n1. `a ^ b` calculates the carry-less sum (e.g., 1+1=0, 1+0=1).\n2. `(a & b) << 1` calculates the carry bits (since only 1+1 creates a carry, which is shifted left by 1).\n3. Repeat this process recursively/iteratively until the carry `b` becomes 0.\nIn Python, integers have arbitrary precision, so we must manually apply a 32-bit mask `0xFFFFFFFF` to simulate the overflow and negative bounds of a standard 32-bit signed integer.",
        "code": """class Solution:
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
"""
    },
    "12_number_of_1_bits.py": {
        "title": "Number of 1 Bits",
        "difficulty": "Easy",
        "key_points": "Bit Manipulation - Brian Kernighan's Algorithm (n & (n - 1))",
        "analysis_intuition": "The standard solution checks the least significant bit (LSB) and shifts right 32 times. However, this always takes 32 iterations, even if the number contains only a single 1 bit.",
        "analysis_derivation": "Brian Kernighan's algorithm optimizes this by clearing the lowest set bit using `n & (n - 1)`. For any number `n`, `n - 1` flips all bits to the right of the lowest set bit (including the set bit itself). Thus, `n & (n - 1)` clears the lowest set bit while keeping all higher bits unchanged. This means the number of iterations equals exactly the number of set bits, which is extremely efficient.",
        "code": """class Solution:
    def hammingWeight(self, n: int) -> int:
        # Time Complexity: O(1) - Iterations match the number of set bits (maximum 32)
        # Space Complexity: O(1)
        count = 0
        while n:
            # Clear the lowest set bit of n
            n = n & (n - 1)
            count += 1
        return count
"""
    },
    "13_counting_bits.py": {
        "title": "Counting Bits",
        "difficulty": "Easy",
        "key_points": "Dynamic Programming + Bit Manipulation",
        "analysis_intuition": "Calculating the number of set bits for each number from 0 to n individually takes O(N log N) or O(32N) time complexity.",
        "analysis_derivation": "To achieve an optimal O(N) time complexity, we can use dynamic programming by reusing previously computed results.\nLet `dp[i]` be the count of 1 bits in the binary representation of `i`.\n1. Parity rules:\n   - If `i` is even, `dp[i] = dp[i >> 1]` because dividing an even number by 2 is a right shift that discards a 0 bit (no change in 1s count).\n   - If `i` is odd, `dp[i] = dp[i >> 1] + 1` because dividing an odd number by 2 is a right shift that discards a 1 bit (adds 1 to the count).\n2. Unified recurrence: `dp[i] = dp[i >> 1] + (i & 1)`. This allows us to compute each state in O(1) time.",
        "code": """from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Time Complexity: O(n) - Single pass from 0 to n
        # Space Complexity: O(1) - Only the output array is allocated
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            # Recurrence: set bits in i equals set bits in i // 2 + LSB of i
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
"""
    },
    "14_missing_number.py": {
        "title": "Missing Number",
        "difficulty": "Easy",
        "key_points": "Bit Manipulation (XOR) / Gauss Sum Formula",
        "analysis_intuition": "Sorting the array and scanning takes O(N log N) time. Using a hash set takes O(N) time but requires O(N) auxiliary space. We need an O(N) time and O(1) space solution.",
        "analysis_derivation": "We can solve this in O(1) space using two methods:\n1. Gauss Sum Formula: Compute the expected sum of numbers from 0 to n using `n * (n + 1) // 2` and subtract the sum of the array. The difference is the missing number. (In languages like C++/Java, overflow must be prevented).\n2. XOR Operation: Since `x ^ x = 0` and `x ^ 0 = x`, if we XOR all indexes `0` to `n` and all values in the array, numbers that appear twice will cancel out to 0, leaving only the missing number that appeared once. This avoids any arithmetic overflow.",
        "code": """from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Time Complexity: O(n) - Single pass through the array
        # Space Complexity: O(1)
        missing = len(nums)
        for i, num in enumerate(nums):
            # XOR indices and numbers to cancel out matches
            missing ^= i ^ num
        return missing
"""
    },
    "15_reverse_bits.py": {
        "title": "Reverse Bits",
        "difficulty": "Easy",
        "key_points": "Bit Manipulation - Shift and Accumulate",
        "analysis_intuition": "We can process the 32 bits of `n` one by one. In each step, we extract the LSB of `n` and shift it to its reversed position in the result.",
        "analysis_derivation": "1. Initialize the result `res = 0`.\n2. Loop 32 times:\n   - Shift the result left by 1 to make space: `res <<= 1`.\n   - Extract the LSB of `n` and bitwise OR it into the result: `res |= (n & 1)`.\n   - Shift `n` right by 1 to process the next bit: `n >>= 1`.\nThis correctly reverses all 32 bits and works for both signed and unsigned representations.",
        "code": """class Solution:
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
"""
    }
}
