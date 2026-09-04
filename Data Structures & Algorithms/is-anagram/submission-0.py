class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = {}
        for char in s:
            if char not in tracker:
                tracker[char] = 0
            tracker[char] += 1
        
        for char in t:
            if char not in tracker:
                return False
            
            tracker[char] -= 1
            if tracker[char] < 0:
                return False

        if any(tracker.values()):
            return False
        
        return True