class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        result = ''
        for i in range(0,len(s), 2*k):
            s[i:k+i] = s[i:k+i][::-1]
        return "".join(s)