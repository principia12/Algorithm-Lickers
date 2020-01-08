# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preprocess(self, root):

        if root.left is None and root.right is None:
            setattr(root, 'num', 1)
        elif root.left is None:
            self.preprocess(root.right)
            setattr(root, 'num', root.right.num + 1)
        elif root.right is None:
            self.preprocess(root.right)
            setattr(root, 'num', root.left.num + 1)
        else:
            self.preprocess(root.right)
            self.preprocess(root.right)
            setattr(root, 'num', root.left.num + root.right.num + 1)

    def flipMatchVoyage(self, root, voyage):
        self.preprocess(root)
        left_num, right_num = self.left.num, self.right.num
        left, right = [], []

        if voyage[0] != val:
            return -1
        if root.left == None and root.right == None:
            return 0

        flag = False
        left, right = voyage[1:1+left_num], voyage[1+left_num:]

        l = self.flipMatchVoyage(root.left, left)
        r = self.flipMatchVoyage(root.right, right)

        if -1 in [l, r]:
            return -1

        return l + r