def gc(dna):
    "gc percentage of a sequence"
    nbases = dna.count('n')+dna.count('N')
    gcpercent = float(dna.count('c')+dna.count('C')+dna.count('g')+dna.count('G'))*100.0/(len(dna)-nbases)
    return gcpercent

def find_stop_codon(dna,frame=0):
    """find all the first in-frame stop codon and return position where it's found"""
    stop_codons=['tga','tag','taa']
    positions = []
    #### Time complexity: T2(n) = O(n/3)
    for i in range(frame,len(dna),3): # one codon has a length of 3 bases, check for every 3 bases
        codon = dna[i:i+3].lower()
        if codon in stop_codons:  #### f(n) = 3
            positions.append(i)
    return positions

def find_start_codon(dna,frame=0):
    """find all the in-frame start codon and returns the position where it's found"""
    positions = []
    start_codons='atg'
    #### Time complexity: T1(n) = O(n/3)
    for i in range(frame,len(dna),3): # check for every 3 bases
        codon = dna[i:i+3].lower()
        if codon == start_codons:
             positions.append(i)
    return positions

def compute_ORF_segments(start_positions, stop_positions):
    """given a list of start codons and stop codons, return a list of segments that can possibly encode proteins"""
    segments = []
    prev_index = 0      # the previous index of stop_positions
    #### Time complexity: T3(m,n) = Ta(m)*Tb(n) = O(m*n)
    for i in range(len(start_positions)):               ### Ta(m)
        for j in range(prev_index,len(stop_positions)): ### Tb(n)
            # stop codon must be after the start codon, and there must be at least 50 codon in between to create protein
            # according to https://www.quora.com/How-many-amino-acids-are-required-in-a-protein-to-call-it-protein
            if stop_positions[j] >= start_positions[i]+153:
                segments.append([start_positions[i],stop_positions[j]])
                prev_index = j
                break
    return segments

def find_ORF(dna):
    """find all the ORF given a DNA string"""
    start_codon_found = False
    stop_codon_found = False
    start_codon_positions = []
    stop_codon_positions = []
    forward_segments = []
    reverse_segments = []
    # check if it has start codon (must have a start codon before stop codon)
    #### Time complexity: T(n) = 3*(T1(n)+T2(n)+T3(m,n)) = 3*(O(n)+O(n)+O(m*n)) = O(mn)
    for i in range(0,3):
        start_codon_positions = find_start_codon(dna, i)         #### T1(n)
        if len(start_codon_positions) != 0:         # if the length is 0, there is no start codon
            start_codon_found = True
            # check if it has stop codon. It must have at least one codon in between start and stop codon
            stop_codon_positions = find_stop_codon(dna,i+6)         #### T2(n)
            if len(stop_codon_positions) != 0:      # same as the previous if statement, length of 0 == no stop codon
                stop_codon_found = True
                forward_segments.append(compute_ORF_segments(start_codon_positions,stop_codon_positions))   #### T3(m,n)
    
    # check the reverse only if no ORF found, otherwise this step is redundant
    if not (start_codon_found and stop_codon_found):
        dna = reverse(dna)
        for i in range(0,3):
            start_codon_positions = find_start_codon(dna, i)
            if len(start_codon_positions) != 0:
                stop_codon_positions = find_stop_codon(dna,i+6)
                if len(stop_codon_positions) != 0:
                    reverse_segments.append(compute_ORF_segments(start_codon_positions,stop_codon_positions))
    return forward_segments, reverse_segments

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