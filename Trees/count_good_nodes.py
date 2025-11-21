# Given the root of a binary tree, find the number of nodes that are good
# A node if good if the path between the root and the node has no nodes
# with a greater value

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root:TreeNode) ->int:
        def dfs(node,curr_max):
            if not node:
                return 0

            left = dfs(node.left, max(curr_max,node.val))
            right = dfs(node.right, max(curr_max,node.val))
            ans = left + right
            if node.val >= curr_max:
                ans += 1

            return ans
        return dfs(root, float("-inf"))

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
answer = solution.goodNodes(root)
print(f'The number of good nodes is {answer}')
                       
