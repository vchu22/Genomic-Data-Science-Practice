"""
    Use Biopython BLAST to search NCBI database for sequences that match the
    sequences in a fasta file.
"""
# Please execute "pip install biopython" before running this script 
import sys
from Bio.Blast import NCBIWWW, NCBIXML

try:
    result_handle = ''
    if (sys.argv[1]):
        print "Reading FASTA file"
        fasta_string = open(sys.argv[1]).read()
        print "Querying NCBI database"
        # first arg: program to use, 2nd arg: database to search against
        result_handle = NCBIWWW.qblast("blastn","nt", fasta_string)
    print "Processing data"
    blast_record = NCBIXML.read(result_handle)
    print "%d alignments:"%len(blast_record.alignments)
    E_VALUE_THRESH = 0.01
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
                if hsp.exepect < E_VALUE_THRESH:
                        print "\n******Alignment*****"
                        print "sequence:",alignment.title
                        print "length:",alignment.length
                        print "e value:",hsp.expect
                        print hsp.query
                        print hsp.match
                        print hsp.sbjct
except IndexError:
    print "Need to include a fasta filename/path in the second argument"