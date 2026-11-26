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



# 2. Average of Levels in Binary Tree
# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
# Example 1: Input: root = [3,9,20,null,null,15,7]. Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
# Example 2: Input: root = [3,9,20,15,7]. Output: [3.00000,14.50000,11.00000]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        if not root: return []

        res, q = [], deque([root])
        while q:
            level_sum = 0
            c = len(q)
            for _ in range(c):
                node = q.popleft()
                level_sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            res.append(level_sum/c)
        
        return res
        

