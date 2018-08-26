from bioseq import dnautil
dnaseq ='acatagagcgnn'
print "Your GC-content takes %f%% of the sequence"%dnautil.gc(dnaseq)
print "Does your sequence has a stop codon? ",("No","Yes")[dnautil.has_stop_codon(dnaseq,0)]
print "Does your sequence contain a stop codon counting from the 2nd position? ",("No","Yes")[dnautil.has_stop_codon(dnaseq,frame=1)]
print "The reverse complement of your sequence is '%s'"%dnautil.reversecomplement(dnaseq)