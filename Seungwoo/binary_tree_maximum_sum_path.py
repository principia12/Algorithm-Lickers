# Definition for a binary tree node.
from pprint import pprint

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def main(line):
    root = stringToTreeNode(line);
    ret = Solution().maxPathSum(root)
    out = str(ret)
    print(out)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def mymax(pos, *args):
    print(pos)
    pprint(args)
    return max(*args)

class Solution:
    def maxRootPathSum(self, root):
        if root.left is None and root.right is None:
            return root.val
        elif root.left is None: # right is not None
            return max(root.val, root.val + self.maxRootPathSum(root.right))
        elif root.right is None:
            return max(root.val, root.val + self.maxRootPathSum(root.left))
        return max(root.val,
                   root.val + self.maxRootPathSum(root.right),
                   root.val + self.maxRootPathSum(root.left), )

    def maxPathSum(self, root):
        return self.result(root)[0]

    def result(self, root):
        # maxPathSum, maxRootPathSum
        if root.left is None and root.right is None:
            return root.val, root.val
        elif root.left is None: # right is not None
            a, b = self.result(root.right)
            return max(a, root.val + b, root.val), max(root.val, root.val + b)
        elif root.right is None:
            a, b = self.result(root.left)
            return max(a, root.val + b, root.val), max(root.val, root.val + b)
        a, b = self.result(root.right)
        c, d = self.result(root.left)
        return max(root.val, a, c, root.val + b, root.val + d, root.val + b + d,), \
               max(root.val, root.val + b, root.val + d,)

main('[-1,5,null,4,null,null,2,-4]')


