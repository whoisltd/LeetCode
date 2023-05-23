class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        s = s.split()

        j = len(s)-1
        i=0
        mid = len(s)//2

        while i < mid:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        return ' '.join(s)