class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        n = nums.copy()
        for i in range(len(n)):
            n[i] = pro
            pro *= nums[i]
        pro = 1
        for j in range(len(n) - 1, -1, -1):
            n[j] *= pro
            pro *= nums[j]
        return n  
