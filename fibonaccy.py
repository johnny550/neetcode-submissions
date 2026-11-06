
class Solution:
    def fib_as_many_as_n(self, n: int) -> int:
        a,b=0,1
        for _ in range(n):
            print(a, end=" ")
            a,b=b,a+b
        print()

    def nth_fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        return self.nth_fib(n-1) + self.nth_fib(n-2)

sol=Solution()
sol.fib_as_many_as_n(4)
print(sol.nth_fib(4))