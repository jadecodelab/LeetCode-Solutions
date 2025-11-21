# given the roots of 2 binary trees p and q
# check if they are the same tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p:TreeNode, q:TreeNode) -> bool:
        # if both of them are empty, then they are the same tree
        if p==None and q==None:
            return True
        # if only one of them is empty, then they are not the same tree
        if p==None or q==None:
            return False

        if p.val != q.val:
            return False

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right


    
# Test case: both trees are empty
solution = Solution()
p1 = None
q1 = None

if solution.isSameTree(p1,q1):
    print("p1 and q1 are the same tree")
else:
    print("p1 and q1 are not the same tree")

#Test case: both trees are not empty
p2 = TreeNode(1, TreeNode(2), TreeNode(3))
q2 = TreeNode(1, TreeNode(2), TreeNode(5))

if solution.isSameTree(p2,q2):
    print("p2 and q2 are the same tree")
else:
    print("p2 and q2 are not the same tree")
