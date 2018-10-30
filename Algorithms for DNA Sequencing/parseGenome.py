'''
    Week 1: Downloading and parsing a genome
'''
import sys

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as file:
        for line in file:
            if not line[0] == '>':
                # if it's not a line that starts with '>', it must be lines containing bases
                genome += line.rstrip()
    return genome
try:
    genome = readGenome(sys.argv[1])
    print genome[:100]
    print len(genome)

    counts = {'A':0, 'C':0, 'G':0, 'T':0}
    for base in genome:
        counts[base] += 1
    print counts

    import collections
    print collections.Counter(genome)
except IndexError:
    print "Please add a fasta file to the command line arguments"