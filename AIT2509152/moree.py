def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)
    
def fib(n):
    if n>=2:
        return fib(n-1) + fib(n-2)
    elif n == 0:
        return 0
    else:
        return 1

print(fac(4))
print(fib(8))