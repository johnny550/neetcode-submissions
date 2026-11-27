class Solution:
    def climbStairs(self, n: int) -> int:
        # improvement over sub 0 and sub 1
        # no need for an entire array, just 
        # keep the last previous values to 
        # calculate the current (next) result
        one, two = 1, 1
        for i in range(n-1):
            temp=one
            one=one+two
            two=temp

        return one
        