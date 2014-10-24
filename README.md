csv2sqlupdate
=============
Creates SQL UPDATE strings for PostgreSQL based on a csv file.

args
====
filename: relative path to the filename of the csv file
tablename: name of the table which is the target of the UPDATE commands

format of input file
====
The input file needs to be a comma-separated CSV file, with the first line as the header.

The header lists:
*name of reference column: the column which contains the unique value used to identify the record to update
*name of column to be updated: the column which contains the value to be updated
*name of column to be updated: (copy of previous)

The body lists:
*unique value used to identify the record to update
*the original value, which will be replaced
*the new value



output
====
