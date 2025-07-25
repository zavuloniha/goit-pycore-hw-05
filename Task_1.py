
def caching_fibonacci() :
    cach = {}
    def fibonacci(n):
        
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cach:
            return cach[n]
        
        cach[n] = fibonacci(n-1) + fibonacci(n-2)
        return cach[n]
    

    return fibonacci

fib = caching_fibonacci()
print(fib(15))