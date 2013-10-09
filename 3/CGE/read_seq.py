'''
This program reads FASTQ file into dictionary,
puts ID as key & [seq, quality] as value

======= usage =======
python read_seq.py [FASTQ file]
'''

def read_file(input_file):

	'''
	Read in file, record and assign ID, sequence and qualtiy value into dictionary(ID=key)
	'''
		
	fastq = {}
	handle = open(input_file)
	for record in SeqIO.parse(handle, 'fastq'):
		fastq[record.id]=[record.seq, record.letter_annotations["phred_quality"]]
	handle.close()
	return fastq


def Trim(sequence, qual):

	'''
	Attempt to read sequence and quality values by window blocks returning possible start and end trim sties 
	'''
	
        QUAL = 50
        LENGTH = 1000 
	WINDOW= len(sequence)/10
	

        trim_start = 0
        trim_end = 0
	trim_sites = []

	average = 0

        for i in range(len(sequence)+1):
		aver = qual[i:(i+WINDOW)]
                if numpy.mean(aver) < QUAL:
			if trim_end == 0:
                        	trim_start = i
			else: 
				trim_end = i
		else:
			pass
		trim_sites.append([trim_start, trim_end])
        return trim_start, trim_end



if __name__ == '__main__':
	
	'''
	runs input file
	print out trim points
	'''
	
	import sys
	import numpy
	from Bio import SeqIO
	
	
	input_file = sys.argv[-1]
	
	fastq = read_file(input_file)
	
	trim = []
	for values in fastq.values():
		#trim.append(values[1])
		trim.append(Trim(values[0]._data,values[1]))

	print trim
