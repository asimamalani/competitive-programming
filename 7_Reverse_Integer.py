"""
7. Reverse Integer
Easy
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the 
value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0

Constraints:
-231 <= x <= 231 - 1
"""

class Solution:
    def reverse(self, x: int) -> int:
        if -9 < x < 9: # input single digit? return as is
            return x
        
        MIN_INT, MAX_INT = -2 ** 31, (2 ** 31) - 1 
        
        is_negative = True if x < 0 else False
        if is_negative:
            x *= -1
        
        reverse = 0
        while x:
            reverse = reverse * 10 + x % 10
            x //= 10
        
        if is_negative:
            reverse *= -1
        
        if MIN_INT <= reverse <= MAX_INT:
            return reverse
        return 0
