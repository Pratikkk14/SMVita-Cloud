class Solution:
    def romanToInt(self,s):
        num = 0
        ToInt = { 'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000 }
        n = len(s)
        for i in range(n):
            if i < n-1 and ToInt[s[i]] < ToInt[s[i+1]]:
                num -= ToInt[s[i]]
            else:
                num += ToInt[s[i]]
        return num
s = "III"
solution = Solution()
print(solution.romanToInt(s))
