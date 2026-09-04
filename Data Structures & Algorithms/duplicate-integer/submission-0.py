class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = set(nums)
        if len(nums) != len(uniques):
            return True
        return False