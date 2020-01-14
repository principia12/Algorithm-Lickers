/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
import kotlin.math.max

class Solution {
    class TreeNode(var `val`: Int) {
        var left: TreeNode? = null
        var right: TreeNode? = null
    }

    fun maxPathSum(root: TreeNode?): Int {
        fun sol(node: TreeNode?): Int {
            if (node == null)
                return 0
            val leftMax = node.`val` + sol(node.left)
            val rightMax = node.`val` + sol(node.right)
            return max(0, max(leftMax, rightMax))
        }

        fun s(node: TreeNode?): Int {
            if (node == null)
                return Int.MIN_VALUE
            var left = 0
            var right = 0
            if (node.left != null) {
                left = max(left, sol(node.left))
            }
            if (node.right != null) {
                right = max(right, sol(node.right))
            }
            val includeNode = node.`val` + left + right
            val leftMax = s(node.left)
            val rightMax = s(node.right)
            return maxOf(includeNode, leftMax, rightMax)
        }

        val result = s(root)
        return result
    }
}