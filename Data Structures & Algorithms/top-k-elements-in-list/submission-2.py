class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        c =dict(Counter(nums))
        c = dict(sorted(c.items(), key=lambda item: item[1]))
        return list(c.keys())[-k:]

        