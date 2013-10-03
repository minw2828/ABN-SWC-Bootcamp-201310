from nucleotide_sequence import DNASequence, RNASequence

def enter_seq():
	x = ''
	while x == '':
		try:
			x = input('Enter your input here: ')
			x = x.upper()
			my_DNASeq = DNASquence(x)
		except:
			pass
	return x

print enter_seq()

