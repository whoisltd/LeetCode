class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = set()
        for i in nums:
            if i not in a:
                a.add(i)
            else: return True
        return False