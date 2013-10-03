raw_string = 'apple'

if len(raw_string) < 20:
    n = 20 - len(raw_string)
    while n > 0:
        raw_string = raw_string + ' '
        n -= 1

print raw_string

# other way to solve the problem:
# ljust(20)
# len('apple\t'.expandtabs(20))
# print '%-25s'%a
