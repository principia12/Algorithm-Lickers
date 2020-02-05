import kotlin.math.max
class Solution {
    
    fun fallingSquares(positions: Array<IntArray>): List<Int> {
        val list = ArrayList<IntArray>()
        val result = ArrayList<Int>()
        var curMax = 0
        list.add(intArrayOf(0, 1000000000, 0))
        for(p in positions) {
            val (start, len) = p
            val end = start + len
            var maxHeight = 0
            for(i in list.size - 1 downTo 0) {
                val line = list[i]
                if(start >= line[1] || end <= line[0])
                    continue
                val height = line[2] + len
                maxHeight = max(maxHeight, height)
            }
            curMax = max(curMax, maxHeight)
            list.add(intArrayOf(start, end, maxHeight))
            result.add(curMax)
            // start ~ end 사이에 있는 빌딩 중 가장 높은 빌딩을 찾아서 갱신.
            // 직사각형을 떨어뜨릴때, 어떤 위치에 구간이 업데이트 될껀지
        }
        return result
        
    }
    
}
