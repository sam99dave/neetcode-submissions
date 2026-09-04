class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for idx, x in enumerate(nums):
            diff = target - x
            if diff in complement:
                return [complement[diff], idx]
            else:
                complement[x] = idx