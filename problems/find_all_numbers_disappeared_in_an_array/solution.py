class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash={}
        result = []
        for i in nums:
            hash[i] = None
        for i in range(1,len(nums)+1):
            if i not in hash.keys():
                result.append(i)
        return result
        
            
            