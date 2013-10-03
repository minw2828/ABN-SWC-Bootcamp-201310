'''
Task Requirement:
=== Step 1 ===
If the user tries to create a NucleotideSequence that contains invalid bases, 
raise an exception that tells them what the problem is
=== Extra credit ===
Write a script that takes user input and creates a DNASequence
- If the input is not a valid sequence, then keep trying until it is
'''


class NucleotideSequence:

    complements = {'G': 'C',
                   'C': 'G',
                   'A': 'T',
                   'T': 'A'}
    
    def __init__(self, sequence):
	assert isinstance(sequence, str)
        assert len(sequence) > 0
	assert sequence.isupper()
	assert set(sequence).difference(set(complements)) == set()
        self.sequence = sequence
        self.base_counts = {}
    
    def base_count(self, base):
	'''return the number of occurrence of the base in the sequence'''
	assert base in set(complements)
        if base in self.base_counts:
            return self.base_counts[base]
        else:
            count = self.sequence.count(base)
            self.base_counts[base] = count
	    assert count < len(self.sequence)
            return count
    
    def gc_content(self):
	'''calculate the GC ratio in the sequence, from 0 to 1'''
        g = self.base_count('G')
        c = self.base_count('C')
	assert float(g+c)/len(self.sequence) in range(0,1)
        return float(g+c)/len(self.sequence)
        
    def reverse_complement(self):
	'''find out the reverse complementary strain of the sequence'''
        rev_c = ""
        for base in self.sequence:
            rev_c = self.complements[base] + rev_c
            
        return rev_c
        
        
class DNASequence(NucleotideSequence):
    '''an inheritance from NucleotideSequence'''
    pass
    
    
class RNASequence(NucleotideSequence):
    '''an ineritnace from NucleotideSequence'''
    complements = {'G': 'C',
                   'C': 'G',
                   'A': 'U',
                   'U': 'A'}

'''
=== Create your own exception ===


class InvalidBaseException(Exception):
	pass
class ZeroLengthSequenceException(Exception):
	pass

=== when implemented ===

raise InvalidBaseException() # it will triger the following except block

try:
	# do something ...
	pass
except InvalidBaseException:
except ZeroLengthSequenceException:
'''


if __name__ == '__main__':

    import sys
    import string

    x = input('Enter your input here: ')
    x = x.upper()
    if set(x).difference(set('ACTGU')) != set():
        raise Exception('Invalid nucleotide input; base: ' + ''.join(set(x).difference(set('ACTGU'))))
    elif 'T' in x and 'U' in x:
        raise Exception('Sequence should either be DNA or RNA')
