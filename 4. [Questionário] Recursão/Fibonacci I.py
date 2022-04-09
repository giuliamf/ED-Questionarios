def fibonacci(x):
    last, seclast, fib = 1, 1, 0
    if x == 1 or x == 2:
        fib = 1

    else:
        count = 3
        while count <= x:
            fib = last + seclast
            seclast = last
            last = fib
            count += 1
    return fib


print(fibonacci(10))

