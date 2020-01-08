"""
In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.
"""


class Solution:
    def canIWin(self, n, N):
        if sum([i+1 for i in range(n)]) < N:
            return False
        if (n+1)%2 == 1:
            return N%(n+1) != 0
        else:
            k = (n+1)//2
            return N%(n+1) == k
s = Solution()
print(s.canIWin(10, 40))
print(s.canIWin(10, 11))
print(s.canIWin(10, 20))
print(s.canIWin(18, 79))
