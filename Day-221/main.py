class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        s = s.lstrip()
        
        if not s:
            return 0
        
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        num = 0
        for char in s:
            if not char.isdigit():
                break
            num = num * 10 + int(char)
        
        num *= sign
        
        if num > INT_MAX:
            return INT_MAX
        elif num < INT_MIN:
            return INT_MIN
        else:
            return num

if __name__ == "__main__":
    s = "42"
    solution = Solution()
    output = solution.myAtoi(s)
    print("Output:", output)
