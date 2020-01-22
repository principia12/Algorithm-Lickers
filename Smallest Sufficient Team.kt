package com.leetcode

import kotlin.math.min
class Solution {
    fun smallestSufficientTeam(req_skills: Array<String>, people: List<List<String>>): IntArray {
        val inf = 100000
        val m = HashMap<String, Int>()
        val countMap = HashMap<String, Int>()
        val result = HashSet<Int>()


        // 포함 관계 제거
        // 반드시 포함해야하는 사람 고려

        val sortedPeople = people
                .mapIndexed { index, list -> index to list}
                .filter { it.second.isNotEmpty() }
                .toSet()
                .distinctBy { it.second }
                .sortedByDescending { it.second.size }

        val numPeople = sortedPeople.size
        val hasParent = BooleanArray(numPeople + 1)

        for(i in 0 until sortedPeople.size) {
            val l = sortedPeople[i].second
            for(j in 0 until sortedPeople.size) {
                if(i==j) continue
                if(sortedPeople[j].second.all { skill -> l.any { it == skill } }) {
                    hasParent[j] = true
                }
            }
        }

        for(i in 0 until req_skills.size) {
            m[req_skills[i]] = 1 shl i
        }


        val peopleBit = IntArray(numPeople){0}

        for(i in 0 until numPeople) {
            for(skill in sortedPeople[i].second) {
                peopleBit[i] = peopleBit[i] or m[skill]!!
            }
        }

        for(i in 0 until sortedPeople.size) {
            for(skill in sortedPeople[i].second) {
                if(!countMap.containsKey(skill)) {
                    countMap[skill] = 0
                }
                countMap[skill] = countMap[skill]!! + 1
            }
        }

        var start = 0
        for(i in 0 until sortedPeople.size) {
            val p = sortedPeople[i]
            if(p.second.any { countMap[it]!! == 1 }) {
                start = start or peopleBit[i]
                result.add(sortedPeople[i].first)
            }
        }

        val dp = Array(1 shl req_skills.size){Array(numPeople){inf}}
        val allSkills = m.map { it.value }.reduce { acc, i -> acc or i }
        var cnt = 0
        var total = inf


        fun solve(state:Int, p:Int, acc:Int): Int {
            if(state == allSkills) {
                total = min(total, acc)
                return 0
            }
            if(acc >= total)
                return inf - 1
            if(p >= numPeople)
                return inf
            if(result.contains(sortedPeople[p].first) || hasParent[p]) {
                return solve(state, p + 1, acc)
            }
            if(dp[state][p] != inf)
                return dp[state][p]
            ++cnt
            val included =  state or peopleBit[p]
            if(included == state)
                return inf
            for(next in p + 1 .. numPeople) {
                if(hasParent[next]) continue
                dp[state][p] = min(dp[state][p], solve(included, next, acc + 1) + 1)
                dp[state][p] = min(dp[state][p], solve(state, next, acc) )
            }
            return dp[state][p]
        }

        fun backTrack(state:Int, p:Int, s:Set<Int>, acc:Int): Set<Int> {
            if(state == allSkills || p >= numPeople)
                return s
            if(result.contains(sortedPeople[p].first) || hasParent[p]) {
                return backTrack(state, p + 1, s, acc)
            }
            val included =  state or peopleBit[p]
            var cur = inf
            var back = false to -1
            for(next in p + 1 .. numPeople) {
                if(hasParent[next]) continue
                val includeDp = solve(included, next, acc + 1)
                val nonIncludeDp = solve(state,next, acc)
                if(cur > includeDp) {
                    back = true to next
                    cur = includeDp
                }
                if(cur >= nonIncludeDp) {
                    back = false to next
                    cur = nonIncludeDp
                }
            }
            if(back.first) {
                return backTrack(included, back.second, s.plus(sortedPeople[p].first), acc + 1)
            }
            return backTrack(state, back.second, s, acc)
        }

//        println(solve(0,0,0))
        val backTrack = backTrack(start, 0, setOf(),0)
        return backTrack.plus(result).toIntArray()
    }
}