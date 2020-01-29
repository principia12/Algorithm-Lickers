package com.leetcode

fun main() {

     class ListNode(var `val`: Int) {
         var next: ListNode? = null
     }

    fun reverseBetween(head: ListNode?, m: Int, n: Int): ListNode? {
        val mid = ( (m-1) + (n-1)) / 2
        val len = (m+n-1)

        fun solve(idx:Int, cur:ListNode?) : ListNode? {
            if(idx > mid || cur == null) {
                return cur
            }
            val opposite = solve(idx + 1, cur.next)
            if( idx < (m-1) || (idx == mid && len % 2 != 0) || opposite == null)
                return opposite
            val temp = cur.`val`
            cur.`val` = opposite.`val`
            opposite.`val` = temp
            return opposite.next
        }
        solve(0, head!!)

        return head
    }

    val head = ListNode(1).apply {
        next = ListNode(2).apply {
            next = ListNode(3).apply {
                next = ListNode(5)
            }
        }
    }
    val reverseBetween = reverseBetween(head, 2, 3)
}