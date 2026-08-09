class Solution:
    def getSum(self, a: int, b: int) -> int:
        # MASK contains 32 ones:
        #
        # 0xFFFFFFFF
        # =
        # 11111111111111111111111111111111
        #
        # Python integers have arbitrary precision, unlike
        # fixed-width 32-bit integers in languages such as Java/C++.
        #
        # We use this mask to keep every intermediate result
        # limited to 32 bits.
        MASK = 0xFFFFFFFF

        # MAX_INT is the largest positive signed 32-bit integer:
        #
        # 0x7FFFFFFF
        # =
        # 01111111111111111111111111111111
        #
        # If the final 32-bit result is larger than MAX_INT,
        # its highest bit is 1, meaning it represents
        # a negative number in two's complement.
        MAX_INT = 0x7FFFFFFF

        # Convert a and b into their 32-bit representations.
        #
        # For positive numbers, this does not change them.
        #
        # For negative numbers, this converts Python's
        # arbitrary-precision representation into the
        # corresponding 32-bit two's complement representation.
        a &= MASK
        b &= MASK

        # Continue until there is no carry left.
        while b != 0:
            # XOR performs binary addition WITHOUT carry.
            #
            # Example:
            #
            # 0 + 0 -> 0
            # 0 + 1 -> 1
            # 1 + 0 -> 1
            # 1 + 1 -> 0
            #
            # This is exactly XOR behavior.
            sum_without_carry = (a ^ b) & MASK

            # AND identifies positions where both bits are 1.
            #
            # Those positions generate a carry.
            #
            # We shift left by one because the carry belongs
            # to the next higher bit.
            carry = ((a & b) << 1) & MASK

            # The original addition a + b has now been transformed
            # into:
            #
            # sum_without_carry + carry
            #
            # Since we still cannot use '+', we repeat the same
            # XOR / AND process in the next iteration.
            a = sum_without_carry
            b = carry

        # At this point b == 0, so no carry remains.
        #
        # 'a' now contains the correct 32-bit result.

        # If a <= MAX_INT, the sign bit is 0,
        # so the result is a normal positive integer.
        if a <= MAX_INT:
            return a

        # Otherwise, the sign bit is 1,
        # meaning this 32-bit pattern represents a negative number.
        #
        # Convert the unsigned 32-bit representation back
        # into Python's negative integer representation.
        #
        # Example:
        #
        # 0xFFFFFFFF represents -1.
        #
        # ~(0xFFFFFFFF ^ 0xFFFFFFFF)
        # = ~0
        # = -1
        return ~(a ^ MASK) 