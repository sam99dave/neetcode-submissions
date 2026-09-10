class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pref = 1
        n = len(nums)
        for i in range(n):
            res[i] = pref
            pref *= nums[i]
        suf = 1
        for i in range(n-1, -1, -1):
            res[i] *= suf
            suf *= nums[i]
        
        return res