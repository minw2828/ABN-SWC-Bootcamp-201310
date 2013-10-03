import sys

try:
    raw = input('Enter your input number here: ')
    if isinstance(raw, int) == False:
        raise Exception
    if raw%2 == 0:
        print 'even'
    else:
        print 'odd'
except Exception:
    print 'Input data should be an integer.'
    exit()


