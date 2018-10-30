'''
    Week 1: Manipulating DNA strings
'''
def longestCommonPrefix(s1,s2):
    i = 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1
    return s1[:i]
print "Longest Common Prefix:",longestCommonPrefix('AACATAT','AACAGAAC')

def match(s1,s2):
    if not len(s1) == len(s2):
        return False
    for i in range(len(s1)):
        if not s1[i] == s2[i]:
            return False
    return True
print ("Not match","Match")[match('ACT','ACT')]
print ("Not match","Match")[match('ACTA','ACT')]
def reverseComplement(s):
    complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t
print reverseComplement('ACCTGCA')