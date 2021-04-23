"""
28. Implement strStr()
Easy
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. 
This is consistent to C's strstr() and Java's indexOf().

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:
Input: haystack = "", needle = ""
Output: 0

Constraints:
0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.
"""

class Solution:
    # sliding window algorithm. time O(m * n), space O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        # quick checks
        if haystack == "" and needle == "":
            return 0
        elif needle == "":
            return 0
        elif haystack == "" or m < n:
            return -1
        i, j, candidate_idx = 0, 0, 0
        while i < m and j < n and (m-i) >= (n-j):
            if haystack[i] != needle[j]:
                i += 1
                continue
            candidate_idx = i
            while i < m and j < n:
                if haystack[i] != needle[j]:
                    break
                i += 1; j += 1
            if j == n: # found candidate
                return candidate_idx
            else:
                i = candidate_idx + 1
                j = 0
        return -1