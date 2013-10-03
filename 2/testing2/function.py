import time
import doctest


def factorial(num):
    '''
    Return the Nth value of factorial sequence
    F(N) = N*(N-1)*(N-2)*...*1
    F(0) = 1, F(1) = 1
    num should be an integer
    '''

    assert isinstance(num, int)
    assert num >= 0
    '''
    the above assert num >= 0 is equaled to the following exception
    But exception gives more specific user defined message
    if num < 0:
        raise Exception("Factorial of a negative integer is not defined")
    '''
    result = 1
    while num>0:
        result *= num
        num -= 1
    return result


def fac(num):
    '''
    Another way to return the Nth value of factorial sequence
    F(N) = N*(N-1)*(N-2)*...*1
    F(0) = 1, F(1) = 1
    n should be an integer

    >>> fac(0)
    1
    >>> fac(1)
    1
    >>> fac(2)
    2
    >>> fac(4)
    24
    >>> fac(5)
    120
    >>> fac(20)
    2432902008176640000
    '''
    assert isinstance(num, int)
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num*fac(num-1)


def fib(n):
    '''
    Returns the Nth value of fibonacci sequence
    F(N) = F(N-1)+F(N-2)
    F(0) = 0, F(1) = 1
    
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(5)
    5
    '''

    assert isinstance(n, int)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


if __name__ == '__main__':
    '''use this so that when exercise1 is imported,
       system will not run the folling codes
    '''

    doctest.testmod()

    start_time = time.time()
    print factorial(3)
    print str(time.time()-start_time)+' seconds'
    
    start_time = time.time()
    print fac(3)
    print str(time.time()-start_time)+' seconds'


    start_time = time.time()
    print fib(5)
    print str(time.time()-start_time)+' seconds'

    '''
    the following does not work as well as doctest.testmod()
    '''

    '''
    tests = [
             [0, 0],
             [1, 1],
             [2, 1],
             [3, 2],
             [5, 5],
             ]
    for input, expected_result in tests:
        assert fib(input) == expected_result
    '''
    
