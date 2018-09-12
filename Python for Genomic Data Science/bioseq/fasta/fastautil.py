def read_fasta_file(filename):
    try:
        file = open(filename,'r')
        seqs = {}
        for line in file:
            line = line.rstrip() # discard \n characters
            # check if it's a header
            if line[0]=='>':    # a header is represented with '>' character in fasta files
                words = line.split()
                name = words[0][1:]         # get the sequence name by getting the first word and removing the '>' at the beginning
                seqs[name] = ''             # create a entry in dictionary for that sequence
            else:
                seqs[name] += line          # appending each line to the sequence
        return seqs
    except IOError:
        print("File %s does not exist",filename)