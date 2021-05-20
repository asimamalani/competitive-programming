"""
101. Symmetric Tree
Easy
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
Follow up: Could you solve it both recursively and iteratively?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # iterative using queue time O(n), space O(n)
    def isSymmetricV1(self, root: TreeNode) -> bool:
        if root.left is None and root.right is None:
            return True
        if root.left is None or root.right is None:
            return False
        q = collections.deque([root.left, root.right])
        while q:
            left_child, right_child = q.popleft(), q.popleft()
            if left_child is None and right_child is None:
                continue
            elif left_child is None or right_child is None:
                return False
            elif left_child.val != right_child.val:
                return False
            else:
                q.extend([left_child.left, right_child.right, left_child.right, right_child.left])
        return True
    
    # recursive time O(n), space O(n)
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def is_mirror(t1: TreeNode, t2: TreeNode):
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            return t1.val == t2.val and is_mirror(t1.left, t2.right) and is_mirror(t2.left, t1.right)
        
        return is_mirror(root, root)
