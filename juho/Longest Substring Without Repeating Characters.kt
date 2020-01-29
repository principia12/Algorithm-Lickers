import java.util.*
import kotlin.math.max
class Solution {
    fun lengthOfLongestSubstring(s: String): Int {
    var result = 0
    val queue = LinkedList<Char> ()
    val check = Array(256){false}
    for(c in s) {
        if(check[c.toInt()]) {
            while(queue.isNotEmpty() && queue.peek() != c) {
                val first = queue.pollFirst()
                check[first.toInt()] = false
            }
            if(queue.isNotEmpty())
                queue.pollFirst()
            queue.add(c)
        } else {
            check[c.toInt()] = true
            queue.add(c)
        }
        result = max(result, queue.size)
    }
    return result
    }
}
