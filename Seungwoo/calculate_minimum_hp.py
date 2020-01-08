from math import inf
from pprint import pprint

class Solution:

    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        res = []

        # res[0][0] will be the ans
        for i in range(m+1):
            if i == m:
                res.append([inf for k in range(n+1)])
            else:
                res.append([])
                for j in range(n+1):
                    if j == n:
                        res[-1].append(inf)
                    else:
                        res[-1].append(0)
        res[m-1][n-1] = max(1, 1-dungeon[-1][-1])
        # print(len(res), len(res[0]))

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if not (i == m-1 and j == n-1):
                    down = res[i+1][j]
                    right = res[i][j+1]
                    cur = dungeon[i][j]
                    res[i][j] = min(max(down-cur, 1), max(right-cur, 1))
        # pprint(res)
        return res[0][0]



s = Solution()
testcase = [[1,-3,3],[0,-2,0],[-3,-3,-3]]
print(s.calculateMinimumHP(testcase))

