class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sums = len(nums)*(len(nums)+1)/2
        sumn = sum(nums)
        return int(sums-sumn)