# problem link: https://leetcode.com/problems/combination-sum

class Solution:
    def __init__(self):
        self.solutions = list()
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:        
        candidates = sorted(candidates)
        self.calculate_sum(candidates, [], target)
        return self.solutions
        
    
    def calculate_sum(self, candidates, result, target):
        if len(candidates) == 0:
            if target == 0:
                self.solutions.append(result)
            return
        
        num = candidates[-1]
        div = target // num
        
        next_candidate = candidates[ : -1]
        
        for i in range(div + 1):
            remain = target - (i * num)
            self.calculate_sum(next_candidate, result + ([num] * i), remain)
        
        
        
            
        
