fasta = {}
header = ''
for line in open('./uniprot_sprot.fasta').readlines():
    if line[0]=='>':
        header = line[1:].strip()
        fasta[header]=''
    else:
        fasta[header]+=line.strip()
        
count = 0
for header in fasta.keys():
    if 'OS=Homo sapiens' in header:
        count += 1
print count
