class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def recursion(op_c, clo_c):
            if op_c == clo_c == n:
                res.append("".join(stack))
                return
            
            if op_c < n:
                stack.append('(')
                recursion(op_c + 1, clo_c)
                stack.pop()
            
            if clo_c < op_c:
                stack.append(')')
                recursion(op_c, clo_c + 1)
                stack.pop()
        
        recursion(0, 0)

        return res
            