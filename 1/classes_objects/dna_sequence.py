import string

class DNASequence:
	def __init__(self, sequence):
		self.sequence = sequence
		self.base_counts = {}

	def base_count(self, base):
		return self.sequence.count(base)

	def gc_content(self):
		g = self.base_count('G')
		c = self.base_count('C')
		return float(g+c)/len(self.sequence)
	
	def reverse_complement(self):
		self.sequence = self.sequence[::-1]
		self.sequence = self.sequence.upper()
		for ch in self.sequence:
			if ch == 'A':
				ch.replace('A', 'T')
			elif ch == 'T':
				ch.replace('T', 'A')
			elif ch == 'C':
				ch.replace('C', 'G')
			elif ch == 'G': 
				ch.replace('G', 'C')
