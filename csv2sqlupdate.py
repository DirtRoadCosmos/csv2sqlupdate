import csv, sys

def escape(string):
    """Escape all single-quotes with a single-quote (postgres escape character)"""
    newString = []
    for character in string:
        if character == '\'':
            newCharacter = '\'\''
        else:
            newCharacter = character
        newString.append(newCharacter)
    return ''.join(newString)

# process the arguments
if len(sys.argv) != 3:
    print 'exiting: incorrect arguments'
    sys.exit()
else:
    fileName = sys.argv[1]
    tableName = sys.argv[2]

# read csv
print 'reading', fileName
with open(fileName, 'rb') as theFile:
    theReader = csv.reader(theFile, delimiter=',')
    rownum = 0
    theOutput = []
    for row in theReader:
        if rownum == 0:
            header = row
            print header
        else:
            thisOutput = ''.join([
                'UPDATE ', tableName, ' SET ', header[1], ' = \'', escape(row[2]),
                '\' WHERE ', header[0], ' = \'', escape(row[0]),
                '\' AND ', header[1], ' = \'', escape(row[1]), '\';\n'
                ])
            theOutput.append(thisOutput)
            print thisOutput
        rownum += 1

# write ouput
outFileName = fileName[:-4] + '_output.sql'
with open(outFileName, 'w') as outputFile:
    for item in theOutput:
        outputFile.write(item)
print 'saved output to', outFileName
