import sys

try:
    raw = input('Enter your input number here: ')
    
    if isinstance(raw,int)==False:
        raise Exception
        
    if raw >0 and raw < 50:
        print 'Minor'
    elif raw >= 50 and raw < 1000:
        print 'Major'
    else:
        print 'Severe'
    
except Exception:
    print 'Input data should be a single integer!'
