def base_count(sequence, base):
    count = 0
    for ch in sequence:
        if ch.upper() == base.upper():
            count += 1
    return count

def gc_content(sequence):
    gc = 0
    for ch in sequence:
        if ch.upper() == 'C' or ch.upper() == 'G':
            gc += 1
    return '%.2f'%(float(gc)/len(sequence))
    
print base_count(sequence, base)
print gc_content(sequence)
