def math_example(a,b):
    result = (a*80+1)*250 + (2*b-250)%2
    
    return result


if __name__ == '__main__':

    import sys
'''    
    try:
        a = input("input values of a: ")
        b = input("input values of b: ")
        if isinstance(a, int) == False or a < 100 or a > 999:
            raise Exception("a")
        elif isinstance(b,int) == False or b < 1000 or b > 9999:
            raise Exception("b")
    except Exception("a"):
        print 'Invalid input. Value a should be an interget between 100 and 999.'
        exit()
    except Exception("b"):
        print 'Invalid input. Value b should be an interget between 1000 and 9999.'
        exit()
    
    print math_example(a,b)
'''

try:
    a = input("input values of a: ")
    if isinstance(a, int) == False or a < 100 or a > 999:
        raise Exception
except Exception:
    print 'Invalid input. Value a should be an interget between 100 and 999.'
    exit()
try:
    b = input("input values of b: ")
    if isinstance(b,int) == False or b < 1000 or b > 9999:
        raise Exception
except Exception:
    print 'Invalid input. Value b should be an interget between 1000 and 9999.'
    exit()
