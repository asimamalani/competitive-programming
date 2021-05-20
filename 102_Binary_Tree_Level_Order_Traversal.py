"""
102. Binary Tree Level Order Traversal
Medium
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # iterative using queue time O(n), space O(n)
    def levelOrderV1(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res
        q = collections.deque([root])
        while q:
            level = []
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
    
    # recursive time O(n), space O(n)
    def levelOrderV2(self, root: TreeNode) -> List[List[int]]:
        result = []
        def traverse(result, d, node):
            if not node:
                return
            if len(result) <= d:
                result.append([node.val])
            else:
                result[d].append(node.val)
            traverse(result, d+1, node.left)
            traverse(result, d+1, node.right)
        
        traverse(result, 0, root)
        return result
