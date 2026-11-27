class Solution:
    # memoization + hashmap
    # o reach step n, you must come from n−1 (1 step) or n−2 (2 steps),
    # so f(n)=f(n−1)+f(n−2). Use a dictionary (memo) to cache previously 
    # computed results and prevent redundant recursive work
    def __init__(self):
        self.memo = {}

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        if n in self.memo:
            return self.memo[n]
 
        self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n - 2)
        return self.memo[n] 
        