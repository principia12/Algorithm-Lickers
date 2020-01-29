    class Solution {
      fun grayCode(n: Int): List<Int> {

          fun solve(n:Int)  : List<Int> {
              if(n == 1)
                  return listOf(0,1)
              if(n==0)
                  return listOf(0)
              return solve(n - 1).plus(solve(n - 1).map { (1 shl (n - 1)) + it }.reversed())
          }
          return solve(n)
      }
    }
