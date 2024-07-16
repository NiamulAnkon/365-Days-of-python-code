class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res, opened = [], 0
        for i in s:
            if i == '(' and opened > 0: res.append(i)
            if i == ')' and opened > 1: res.append(i)
            opened += 1 if i == '(' else -1

        return"".join(res)