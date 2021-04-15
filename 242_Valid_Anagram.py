"""
242. Valid Anagram
Easy
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

class Solution:
    # Sorting time O(nlogn), space O(n+m)
    def isAnagramV1(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    # Counter time O(n+m), space O(n+m)
    def isAnagramV2(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
    
    # Const space array time O(n+m), space O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        # quick checks for performance and edge cases
        if s is t:
            return True
        if len(s) != len(t):
            return False
        if s == t:
            return True
        
        count = [0] * 26
        
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        for c in t:
            count[ord(c) - ord('a')] -= 1
            if count[ord(c) - ord('a')] < 0:
                return False
        return True
