import math

class Solution:
    def minimum(self, lst, key):
        cur_min = math.inf
        res = None
        for idx, elem in enumerate(lst):
            k = key(elem)
            if k < cur_min:
                cur_min = k
                res = elem
        return res

    def smallestSufficientTeam(self, req_skills, people):
        # base case for recursion
        if req_skills == []:
            return []
        for idx, person in enumerate(people):
            if set(person) == set(req_skills): # when a person have every required skills
                return [idx]
        else: # if there is no such superman :(
            possible_teams = []

            for idx, person in enumerate(people):
                if person == []:
                    continue
                rec_ans = self.smallestSufficientTeam(\
                        [s for s in req_skills if s not in person],
                        people[:idx] + people[idx+1:])
                for r_idx, p_idx in enumerate(rec_ans):
                    if p_idx >= idx:
                        rec_ans[r_idx] = p_idx + 1
                possible_teams.append([idx] + rec_ans)

            return self.minimum(possible_teams, key = len)


req_skills = ["algorithms","math","java","reactjs","csharp","aws"]
people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]

req_skills = ["gvp","jgpzzicdvgxlfix","kqcrfwerywbwi","jzukdzrfgvdbrunw","k"]
people = [[],[],[],[],["jgpzzicdvgxlfix"],["jgpzzicdvgxlfix","k"],["jgpzzicdvgxlfix","kqcrfwerywbwi"],["gvp"],["jzukdzrfgvdbrunw"],["gvp","kqcrfwerywbwi"]]


req_skills = ["cdkpfwkhlfbps","hnvepiymrmb","cqrdrqty","pxivftxovnpf","uefdllzzmvpaicyl","idsyvyl"]
people = [[],["hnvepiymrmb"],["uefdllzzmvpaicyl"],[],["hnvepiymrmb","cqrdrqty"],["pxivftxovnpf"],["hnvepiymrmb","pxivftxovnpf"],["hnvepiymrmb"],["cdkpfwkhlfbps"],["idsyvyl"],[],["cdkpfwkhlfbps","uefdllzzmvpaicyl"],["cdkpfwkhlfbps","uefdllzzmvpaicyl"],["pxivftxovnpf","uefdllzzmvpaicyl"],[],["cqrdrqty"],[],["cqrdrqty","pxivftxovnpf","idsyvyl"],["hnvepiymrmb","idsyvyl"],[]]
s = Solution()

# print(s.minimum([1,2,3,4,1,2,3,1], key = lambda x:x%4))
print(s.smallestSufficientTeam(req_skills, people))
# print(list(s.choose_l_items(list(range(10)), 2)))
