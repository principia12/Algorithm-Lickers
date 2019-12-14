package leetcode

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

fun main() {


    fun flipMatchVoyage(root: TreeNode?, voyage: IntArray): List<Int> {

        val countMap = HashMap<TreeNode, Int>()

        fun countChild(node:TreeNode?) : Int {
            if(node == null) return 0
            if(countMap.containsKey(node)) return countMap[node]!!
            countMap[node] = countChild(node.left) + countChild(node.right) + 2
            if(node.left == null)
                countMap[node] = countMap[node]!! - 1
            if(node.right == null)
                countMap[node] = countMap[node]!! - 1
            return countMap[node]!!
        }

        fun flip(node:TreeNode) {
            val temp :TreeNode? = node.left
            node.left = node.right
            node.right = temp
        }

        fun s(cur:TreeNode?, idx:Int, result:List<Int>): List<Int> {
            if(cur == null)
                return result
            if(cur.`val` != voyage[idx]) return listOf(-1)
            var next = result
            var leftIdx = idx + 1
            var rightIdx = idx + 1
            if(cur.left != null && cur.right != null) {
                rightIdx = countChild(cur.left) + 2 + idx
                val lVal = voyage[leftIdx]
                val rVal = voyage[rightIdx]
                if(cur.left!!.`val` != lVal || cur.right!!.`val` != rVal) {
                    rightIdx = countChild(cur.right) + 2 + idx
                    flip(cur)
                    next = result.plus(cur.`val`)
                }
            }
            val left = s(cur.left, leftIdx, next)
            if(left.find { it == -1 } != null)
                return left
            val right = s(cur.right, rightIdx, left)
            return right
        }

        countChild(root)
        return s(root, 0, listOf())
    }

    val root = TreeNode(2)
//    root.left = TreeNode(1)
    root.left = TreeNode(3).apply {
        left = TreeNode(4)
        right = TreeNode(5).apply {
            left = TreeNode(1)
        }
    }


    flipMatchVoyage(root, intArrayOf(2,3,4,5,1))

}