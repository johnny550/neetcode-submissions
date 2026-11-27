class Solution:
    def climbStairs(self, n: int) -> int:
        # for loop
        dp=[i for i in range(n+1)]
        i=n
        for i in range(n, -1, -1):
            if i == n or i== n-1:
                dp[i] = 1
            else:
                dp[i] = dp[i+1] + dp[i+2]
        return dp[0]
        