import csv, sys

# process the arguments
print 'processing the arguments'

def escape(string):
    newString = []
    for character in string:
        if character == '\'':
            newCharacter = '\'\''
        else:
            newCharacter = character
        newString.append(newCharacter)
    return ''.join(newString)
    
if len(sys.argv) != 3:
    sys.exit()
else:
    fileName = sys.argv[1]
    tableName = sys.argv[2]

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

with open(fileName[:-4] + '_output.sql', 'w') as outputFile:
    for item in theOutput:
        outputFile.write(item)
