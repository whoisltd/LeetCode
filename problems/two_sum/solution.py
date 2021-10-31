class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in hashmap:
                return [i, hashmap[a]]
            hashmap[nums[i]] = i
            