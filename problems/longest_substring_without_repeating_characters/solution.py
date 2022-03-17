class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        ans = 0
        table = {}
        for j in range(len(s)):
            if s[j] in table:
                i = max(table[s[j]], i)
            table[s[j]] = j+1
            ans = max(ans, j - i+1)
        return ans