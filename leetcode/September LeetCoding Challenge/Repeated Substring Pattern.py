class Solution:
    def repeatedSubstringPattern(self, s):
        N = len(s)
        for i in range(1, N//2+1):
            if N % i == 0 and s[:i]* (N//i) == s:
                return True
        return False