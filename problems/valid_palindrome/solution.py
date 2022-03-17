class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''.join(filter(str.isalnum, s.lower()))
        for i in range(len(a)//2):
            if a[i] == a[len(a)-1-i]:
                continue
            else:
                return False
        return True

        