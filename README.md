##csv2sqlupdate

Creates SQL UPDATE strings for PostgreSQL based on a csv file.

###args

* filename: relative path to the filename of the csv file
* tablename: name of the table which is the target of the UPDATE commands

###format of input file

The input file needs to be a comma-separated CSV file, with the first line as the header.

The header lists:
* name of reference column: the column which contains the unique value used to identify the record to update
* name of column to be updated: the column which contains the value to be updated
* name of column to be updated: (copy of previous)

NOTE: The column names indicated in the second and third positions of the header should be the same. This corresponds to the data in the body below those header items: the second item in each row of the body contains the "old" value to be replaced, and the third item in each row contains the "new" value. This is an intentional piece of security, to be sure the change is intended.

The body lists:
* unique value used to identify the record to update
* the original value, which will be replaced
* the new value


###output

The script creates a text file in the same directory as the input file. The output file name is "[input base]_output.sql".

The output file contains SQL update statements.

Single quotes in value strings are escaped with another single quote.


###example

INPUT:
```
+------------+----------+--------------+
|   geoid    | townname |   townname   |
+------------+----------+--------------+
| 5001300700 | Alburg   | Alburgh      |
| 5000902162 | Avery's  | Avery's Gore |
| 5002303250 | Barre    | Barre Town   |
| 5002303175 | Barre    | Barre City   |
+------------+----------+--------------+
```

INVOKE:
```
python csv2sqlupdate.py data.csv towns_hist
```

OUTPUT:
```
UPDATE towns_hist SET townname = 'Alburgh' WHERE geoid = '5001300700' AND townname = 'Alburg';
UPDATE towns_hist SET townname = 'Avery''s Gore' WHERE geoid = '5000902162' AND townname = 'Avery''s';
UPDATE towns_hist SET townname = 'Barre Town' WHERE geoid = '5002303250' AND townname = 'Barre';
UPDATE towns_hist SET townname = 'Barre City' WHERE geoid = '5002303175' AND townname = 'Barre';
```
