package leetcode

import kotlin.math.abs

fun main() {
    fun judgePoint24(nums: IntArray): Boolean {
        fun comb(l:Set<Double>, r:Set<Double>): HashSet<Double> {
            val result = HashSet<Double>()
            for(a in l) {
                for(b in r) {
                    result.add(a * b)
                    result.add(a / b)
                    result.add(a + b)
                    result.add(a - b)
                }
            }
            return result
        }

        fun solve(nums:IntArray): HashSet<Double> {
            if(nums.size == 1)
                return hashSetOf(nums[0].toDouble())
            val bound = nums.size / 2 - 1
            val result = HashSet<Double>()
            // 8 / 0.3333333333333335
            // 3 8 3 => 0.3333333333333335
            // 8 /  (3 - 8 / 3)
            for(i in 0 .. bound) {
                val l = solve(nums.copyOfRange(0, i+1))
                val r = solve(nums.copyOfRange(i+1,nums.size))
                val set = comb(l,r)
                result.addAll(set)
            }
            return result
        }

        fun permutation(list:List<Int>, checked:BooleanArray): Boolean {
            if(list.size == nums.size) {
                val set = solve(list.toIntArray())
                return set.any { abs(it -24.0) <= 0.0000000001 }
            }
            for(i in 0 until nums.size) {
                if(checked[i]) continue
                checked[i] = true
                if(permutation(list.plus(nums[i]), checked))
                    return true
                checked[i] = false
            }
            return false
        }
        val result = permutation(emptyList(), BooleanArray(4))
        return result
    }
    println(judgePoint24(intArrayOf(3,3,8,8)))
}