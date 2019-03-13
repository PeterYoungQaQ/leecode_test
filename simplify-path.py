# coding=utf-8
# @Time: 3/13/2019 3:05 PM


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack, i, ans = [], 0, ''
        while i < len(path):
            j = i + 1
            while j < len(path) and path[j] != '/':
                j += 1
            # tmp为路径名
            tmp = path[i + 1:j]
            if tmp != '':
                if tmp == '..':
                    if stack:
                        stack.pop()
                elif tmp != '.':
                    stack.append(tmp)
            i = j
        if not stack:
            return '/'
        for k in stack:
            ans += '/' + k
        return ans


print(Solution().simplifyPath("/a/./b/../../c/"))