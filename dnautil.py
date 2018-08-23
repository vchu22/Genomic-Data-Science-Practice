def gc(dna):
    "gc percentage of a sequence"
    nbases = dna.count('n')+dna.count('N')
    gcpercent = float(dna.count('c')+dna.count('C')+dna.count('g')+dna.count('G'))*100.0/(len(dna)-nbases)
    return gcpercent

def has_stop_codon(dna,frame=0):
    "checks if there's a in-frame stop codon"
    stop_codon_found = False
    stop_codons=['tga','tag','taa']
    for i in range(frame,len(dna),3): # check for every 3 bases
        codon = dna[i:i+3].lower()
        if codon in stop_codons:
            stop_codon_found = True
            break
    return stop_codon_found

def reversecomplement(seq):
    "returns reverse complement of a sequence"
    return complement(reverse(seq))

def reverse(dna):
    "returns reverse of a string"
    return dna[::-1] # the last argument indicate counting each letter in reverse order

def complement(dna):
    """returns the complement of a sequence"""
    basecomplement = {'A':'T','C':'G','G':'C','T':'A','N':'N',
                        'a':'t','c':'g','g':'c','t':'a','n':'n'}
    letters = list(dna)     # turn a string into a list of characters
    letters = [basecomplement[base] for base in letters] # iterate through each base in the sequence and store the complement
    return ''.join(letters) # concatenate all list elements into string