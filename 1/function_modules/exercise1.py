import time

# calculate factorial

def factorial(num):
    result = 1
    while num>0:
        result *= num
        num -= 1
    return result
start_time = time.time()
print factorial(3)
print str(time.time()-start_time)+' seconds'

# another way to calculate factorial

def fac(num):
    if num == 1:
        return 1
    else:
        return num*fac(num-1)
start_time = time.time()
print fac(3)
print str(time.time()-start_time)+' seconds'

# calculate fibonacci number

def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
start_time = time.time()
print fib(5)
print str(time.time()-start_time)+' seconds'
