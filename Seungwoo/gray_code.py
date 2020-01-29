class Solution:
    def modulate(self, code, key):
        assert len(code) == len(key)
        for idx, k in enumerate(key):
            if k:
                code[idx] = 1 - code[idx]
        return code

    def seq2num(self, code):
        res = 0
        for elem in code:
            res = res * 2 + elem
        return res

    def gray(self, n):
        if n == 0:
            return [[0]]
        elif n == 1:
            return [[0], [1]]

        first_half = self.gray(n-1)
        modulate_code = first_half[-1]
        print(first_half, 123213)

        second_half = [self.modulate(e, modulate_code) for e in first_half]
        # second_half = [self.modulate(e, modulate_code) for e in self.gray(n-1)]
        print(first_half, 99923213)
        return [[0] + e for e in first_half[::-1]] + [[1] + e for e in second_half]

    def grayCode(self, n):
        return [self.seq2num(e) for e in self.gray(n)]


s = Solution()
from pprint import pprint
pprint(s.gray(2))
# pprint(s.grayCode(2))
