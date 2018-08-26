"""
    Read sequence from fasta file and find the open reading frames
"""
from bioseq.fasta import fastautil
from bioseq.dnautil import *
fasta = fastautil.read_fasta_file('example.fasta')
maxlen = 0
maxleni = 0
for k in fasta:
    seq = fasta[k]
    segments = find_ORF(seq)
    forword_ORF = segments[0]
    reverse_ORF = segments[1]

    print "Sequence %s: Num of forward segments %s , Reverse segments %s "%(k,len(forword_ORF),len(reverse_ORF))
    if (len(forword_ORF) > 0):
        r = (3,len(forword_ORF))[len(forword_ORF) < 3]
        for i in range(0,r):
            print "Fowards segments - Reading frame %d: %s"%(i+1,forword_ORF[i])
    if (len(reverse_ORF) > 0):
        r = (3,len(reverse_ORF))[len(reverse_ORF) < 3]
        for i in range(0,r):
            print "Reverse segments - Reading frame %d: %s"%(i+1,reverse_ORF[i])
    print