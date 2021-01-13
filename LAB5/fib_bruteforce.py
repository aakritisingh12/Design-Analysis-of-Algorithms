# brute - force approach
call = 0
num = int(input("Enter n: "))

# starting Fibonacci series from 1
def Fibonacci(n):
    global call
    if n <= 2:
        call += 1
        return 1
    else:
        call += 1
        return Fibonacci(n - 1) + Fibonacci(n - 2)


print("The nth fibonacci number is ", Fibonacci(num))
print("No of times Fibonacci function is called is ", call)
