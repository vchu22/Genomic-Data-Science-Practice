
# practice with external file
try:
    file=open('example.txt','r')
    print "File content"
    for line in file:
        print line.strip('\n')
    
    print "\nfile.read() "
    file.seek(0)
    print file.read()

    file.seek(0)
    print "\n1st line ",file.readline().strip('\n')
    print "2nd line ",file.readline().strip('\n')
    file.close()
    file = open('example.txt', 'a')
    file.write('\nThis is the extra line')
    file.close()
except IOError:
    print "file does not exist"