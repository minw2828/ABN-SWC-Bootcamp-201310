sequence = 'GGGGGGGGGGGAAAAAAAAAATTTTTTTTTATATACCCCCCCCCCCCCCCCCCCCGCCC'

count = {}
for ch in sequence.upper():
    if ch not in count.keys():
        count[ch]=0
    else:
        count[ch]+=1
        
print count


GC_content = float(count['C']+count['G'])/len(sequence)
print '%.2f'%GC_content


