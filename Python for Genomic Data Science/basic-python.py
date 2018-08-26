dnaseq = 'aagctaacgtaag'.upper()
print 'Your DNA sequence is '+dnaseq
print "The length is",len(dnaseq)
print "It contains",dnaseq.count('A'),"A's"
print "The first occurence of AA is at position",dnaseq.find('AA')+1
print "The second position is at",dnaseq.find('AA',1)+1
print "The last position is at",dnaseq.rfind('AA')+1
perc = dnaseq.count('A')* 100.0 / len(dnaseq)
print "A's take about %.3f %% of the DNA sequence" %perc