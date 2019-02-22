
class Solution:
    def longestValidParentheses(self, s: 'str') -> 'int':
        ans = 0
        n = len(s)
        stack = []
        st = 0
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    st = i + 1
                    continue
                else:
                    stack.pop()
                    if len(stack) == 0:
                        ans = max(ans, i-st+1)
                    else:
                        ans = max(ans, i-stack[-1])
        return ans
        
print(Solution.longestValidParentheses(0,')()())'))
