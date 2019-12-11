class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return [[]]
        candidates.sort()
        return self.combsum(candidates, target)
        
    def combsum(self, candidates, target):
        num = candidates[0]
        if len(candidates) == 1:
            if target % num == 0:
                return [[num for i in range(target//num)]]
            else:
                return None
        else:
            res = []
            for q in range(target//num + 1):
                remainder = target - num * q
                head = [num for i in range(q)]
                tails = self.combsum(candidates[1:], remainder)
                
                if tails is not None:
                    for tail in tails:
                        res.append(head + tail)
            
            return res