"""
14. Longest Common Prefix
Easy
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""

class Solution:
    # vertical scanning time O(S), S is sum of all chars in all strings, space O(1)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        n, min_len = len(strs), len(min(strs, key=len))
        for i in range(min_len):
            ch = strs[0][i]
            for j in range(1, n):
                if strs[j][i] != ch:
                    return strs[0][:i]
        return strs[0][:min_len]
