import kotlin.math.max
import kotlin.math.min
class Solution {
    fun kConcatenationMaxSum(arr: IntArray, k: Int): Int {
        val sum = arr.sum().toLong()
        var mergeMax = 0L
        var curSum = 0L
        var cnt = if(k > 1) 2 * arr.size else arr.size

        for(i in 0 until cnt) {
            val d = arr[i % arr.size].toLong()
            curSum += d
            if(curSum < 0)
                curSum = 0
            mergeMax = max(mergeMax, curSum)
        }
        return ((mergeMax + max(0,(k - 2) * sum)) % 1000000007L).toInt()
    }
}
