class Solution:
    def solve(self, n):
        if n == 1:
            return n
        else:
            return n * self.solve(n-1)
n=3
s = Solution()
print(s.solve(n))