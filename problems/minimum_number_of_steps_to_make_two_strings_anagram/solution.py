class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a = set(s)
        result = 0
        c = 0
        for i in a:
            c = s.count(i) - t.count(i)
            if c>0:
                result += c
        return result
        