#Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

# Return the maximum product you can get.

 

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.


def integerBreak(self, n:int) -> int:
    if n < 4:
        return n -1
    elif n % 3 == 0:  #6=> 3,3=>9
        return 3 ** (n // 3 )
    elif n % 3 == 1: #10=>3,3,4=>36
        return 4 * (3 ** ((n // 3 )-1))
    else:   # 14>3,3,3,3,2
        return 3 ** (n // 3) * 2
