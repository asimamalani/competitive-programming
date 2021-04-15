"""
125. Valid Palindrome
Easy
Given a string s, determine if it is a palindrome, considering only alphanumeric characters 
and ignoring cases.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

class Solution:
    # brute force multiple pass O(n), space O(n)
    def isPalindromeV1(self, s: str) -> bool:
        clean_s = re.sub("[^0-9a-z]+", "", s.lower())
        return clean_s == clean_s[::-1]
    
    # optimization single pass. two pointer time O(n), space O(1)
    def isPalindromeV2(self, s: str) -> bool:
        n = len(s)
        if n == 1:
            return True
        i, j = 0, n-1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if i < j and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
