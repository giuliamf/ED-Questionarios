def fib(x):
    if x <= 1:
        return x
    else:
        return fib(x - 1) + fib(x - 2)


def fibonacci(n):
    return [fib(i) for i in range(n)]


print(fibonacci(10))



