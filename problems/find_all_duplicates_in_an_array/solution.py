class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hash = {}
        ls=[]
        for i in range(len(nums)):
            if nums[i] not in hash.keys():
                hash[nums[i]] = 1
            else:
                ls.append(nums[i])
        return ls
                
            