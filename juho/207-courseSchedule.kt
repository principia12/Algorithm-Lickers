package com.leetcode

fun main() {

    fun canFinish(numCourses: Int, prerequisites: Array<IntArray>): Boolean {
        val m = HashMap<Int, HashSet<Int>>()
        val NON_VISIT = 0
        val states = IntArray(numCourses){NON_VISIT}
        val PROGRESS = 1
        val DONE = 2

        for(i in 0 until numCourses){
            m[i] = HashSet()
        }
        for(depend in prerequisites) {
            val from = depend[0]
            val to = depend[1]
            m[from]!!.add(to)
        }

        fun dfs(cur:Int): Boolean {
            if(states[cur] == DONE) return true
            if(states[cur] == PROGRESS) return false
            states[cur] = PROGRESS
            for(next in m[cur]!!) {
                if(!dfs(next)) return false
            }
            states[cur]=DONE
            return true
        }

        for(course in 0 until numCourses) {
            if(!dfs(course)) return false
        }

        return true
    }

    println(canFinish(4, arrayOf(intArrayOf(0,1), intArrayOf(1,3), intArrayOf(3,1), intArrayOf(3,2))))

}