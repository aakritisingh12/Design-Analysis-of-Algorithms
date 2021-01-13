# bottom up approach
num = int(input("Enter n: "))
fib = {}


def Fibonacci(n, fib):
    for k in range(1, n + 1): # starting from 1
        if k <= 2:
            f = 1
        else:
            f = fib[k - 1] + fib[k - 2]
        fib[k] = f
    # print(fib)
    return fib[n]


print("The nth fibonacci number is ", Fibonacci(num, fib))
