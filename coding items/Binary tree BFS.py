# 1. Binary Tree Right Side View
# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
# Example 1: Input: root = [1,2,3,null,5,null,4]. Output: [1,3,4]
# Example 2: Input: root = [1,2,3,4,null,null,null,5]. Output: [1,3,4,5]
# Example 3: Input: root = [1,null,3]. Output: [1,3]
# Example 4: Input: root = []. Output: []


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        res, q = [], deque([root])

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i == size -1: # if last node of this level ->visible
                    res.append(node.val)
                # push children
                if node.left: 
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res




