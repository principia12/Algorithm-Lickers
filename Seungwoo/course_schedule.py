# do toposort. if fail, return False. if success, return True

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """Kahn's algorithm in wikipedia"""

        graph = defaultdict(lambda :[])
        in_degree = defaultdict(lambda :0)

        for from_course, to_course in prerequisites:
            graph[from_course].append(to_course)
            in_degree[to_course] += 1

        S = []
        visited_nodes = 0

        for n in range(numCourses):
            if in_degree[n] == 0:
                S.append(n)

        if S == []:
            return False

        while S != []:
            n = S.pop()
            visited_nodes += 1
            print(n)
            for m in graph[n]:
                in_degree[m] -= 1
                if in_degree[m] == 0:
                    S.append(m)

        return visited_nodes == numCourses

s = Solution()
print(s.canFinish(2, [[0,1], [1,0]]))





