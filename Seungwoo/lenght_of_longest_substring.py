class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=0
        res = [0]
        d={}

        for idx, elem in enumerate(s):
            if elem not in d:
                d[elem] = idx
            else:
                cand = d[elem]
                if cand < start:
                    d[elem] = idx
                else:
                    res.append(idx - start)
                    start = cand + 1
                    d[elem] = idx

        res.append(len(s)-start)

        return max(res)