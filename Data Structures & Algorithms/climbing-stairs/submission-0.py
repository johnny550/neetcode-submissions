class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[i for i in range(n+1)]
        i=n
        while i<=n and i > -1:
            if i == n or i== n-1:
                dp[i] = 1
            else:
                dp[i] = dp[i+1] + dp[i+2]
            i-=1
        return dp[0]
        