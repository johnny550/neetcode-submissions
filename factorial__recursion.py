# recursion
def factorial(n:int)->int:
    if n<=1:
        return 1
    return n * factorial(n-1)

# with a loop
def factorial_loop(n: int) -> int:
    res=1
    while n> 1:
        res = res * n
        n-=1
    return res
print(factorial(5))
print(factorial_loop(5))