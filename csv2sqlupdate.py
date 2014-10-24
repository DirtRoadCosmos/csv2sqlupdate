import csv

# process the arguments
if len(sys.argv) != 2:
    sys.exit()
else:
    filename = sys.argv[1]
    tablename = sys.arv[2]

with open(filename, 'rb') as csvfile:
    theReader = csv.reader(csvfile, delimiter=',')
    for row in theReader:
        thisOutput = ['UPDATE', tablename, 'SET', head1, '/= /'', row[0], '/'', 'WHERE', head2, '/= /'', row[1], '/';']
        theOutput.append(''.join(thisOutput))
        print thisOutput

        