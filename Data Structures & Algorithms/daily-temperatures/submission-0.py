class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for idx, t in enumerate(temperatures):
            while stack and t > stack[-1][-1]:
                stackIdx, stackT = stack.pop()
                res[stackIdx] = idx - stackIdx
            
            stack.append((idx, t))
        
        return res
