"""
387. First Unique Character in a String
Easy
Given a string s, return the first non-repeating character in it and return its index. 
If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.
"""

class Solution:
    def firstUniqCharV1(self, s: str) -> int:
        count = collections.Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
    
    def firstUniqCharV2(self, s: str) -> int:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1
        for i, c in enumerate(s):
            if freq[ord(c) - ord('a')] == 1:
                return i
        return -1
    
    def firstUniqCharV3(self, s: str) -> int:
        d = {}
        seen = set()
        for idx, ch in enumerate(s):
            if ch not in seen:
                seen.add(ch)
                d[ch] = idx
            elif ch in d:
                del d[ch]
        return min(d.values()) if len(d) > 0 else -1
