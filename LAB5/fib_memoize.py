# dynamic programming using memorisation
call = 0
mem = {}
num = int(input("Enter n: "))

# starting Fibonacci series from 1
def fib(n, memo):
    global call
    if n in memo:
        return memo[n]
    if n <= 2:
        f = 1
        call += 1
    else:
        f = fib(n - 1, memo) + fib(n - 2, memo)
        call += 1
    memo[n] = f
    return f


print("The nth fibonacci number is ", fib(num, mem))
print("No of times Fibonacci function is called is ", call)
