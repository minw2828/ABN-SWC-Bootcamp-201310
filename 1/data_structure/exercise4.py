raw_string = 'Apple, banana, and cherry.'
print len(set(raw_string))


s1 = 'you are an idoit'
s2 = 'I am very happy'

print set(s1).intersection(set(s2))
print set(s1).symmetric_difference(set(s2))
