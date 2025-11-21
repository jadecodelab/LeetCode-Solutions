# Given a root of a binary tree and an integer targetSum,
# return True if there exists a path from the root to a leaf
# such that the sum of the nodes on the path is equal to targetSum

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root:[TreeNode], targetSum:int)-> bool:
        def dfs(node,curr):
            if not node:
                return False

            if node.left == None and node.right == None: #leaf node
                return(curr + node.val)== targetSum

            curr += node.val
            left = dfs(node.left, curr)
            right = dfs(node.right, curr)
            return left or right

        return dfs(root,0)

# Test case
#       1
#       /\
#      2  3
#     /\
#    4  5
#        \
#         6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.right = TreeNode(6)

solution = Solution()
targetSum = 7
answer = solution.hasPathSum(root,targetSum)
if answer:
    print(f'There exists a path that sum of the nodes on the path is equal to {targetSum}')
else:
    print(f"There's NO path that sum of the nodes on the path is equal to {targetSum}")
