class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_i = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in hash_i:
                return [i, hash_i[a]]
            hash_i[nums[i]] = i