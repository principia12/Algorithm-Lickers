# submission: https://leetcode.com/submissions/detail/285127984/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtracking(candidates, remain, path):
            for i, candidate in enumerate(candidates):
                if remain-candidate == 0:
                    solutions.append(path+[candidate])
                elif remain-candidate > 0:
                    backtracking(candidates[i:], remain-candidate, path+[candidate])
        
        solutions=[]
        backtracking(candidates, target, list())
        return solutions
