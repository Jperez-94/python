##########################
# Author: Jose Luis Perez
# Date: 24/10/2020
##########################

import pandas
import os.path
import sys

#################################################
# Basic use of the python library pandas
# It looks for an especific key word in the
# DataFrame and replace it with the new key
# generating a copy of the original DataFrame
# and giving a new file as output
#################################################


print("File name:")

# @name_in   ----> Nombre del fichero con los datos
# (we add csv or xlsx depending on the type of file we want to read from)
name_in = input()
name_in += ".csv"
#name_in += ".xlsx"

# @key -> Word the script has to look for
print("Key word:")
key = input()

# @new_key -> Word the script has to use to replace the key 
print("New key:")
new_key = input()

## Check the path file exist
try:
    if(os.path.isfile(name_in) != True):
        raise Exception()
except Exception:
    print("\nERROR: The file name path doesn't exist")
    sys.exit()

## Open the file an create a DataFrame with the information
# (we use one or another depending on the extension)
file_in = pandas.read_csv(name_in)
#file_in = pandas.read_excel(name_in)

## Open the file where we are going to save the changes
file_out = open("pandasReplaceOutput.csv", "w")

# @i -> Index of the row
# @j -> Index o f the column
for i in range(file_in.shape[0]):
    row = file_in.iloc[i]
    for j in range(row.size):
        if row[j] == key:
            file_out.write(str(new_key))
        else:
            file_out.write(str(row[j]))
        file_out.write(", ")
    file_out.write("\n")

file_out.close()
print("\n The keyword " + key + " has been replace with the word " + new_key + "\n")