##########################
# Author: Jose Luis Perez
# Date: 23/10/2020
##########################

import pandas
import os.path
import sys

#################################################
# Basic use of the python library pandas
# It looks for an especific key word in the
# DataFrame giving back the information you need
# This example gives back the repetitions of the
# key and the position of each one in the file
#################################################



# @name_in   ----> Nombre del fichero con los datos
# (we add csv or xlsx depending on the type of file we want to read from)
name_in = input('File name:\n')
name_in += ".csv"
#name_in += ".xlsx"

# @key -> Word the script has to look for
key = input('Key word:\n')

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

repetitions = 0

# @i -> Index of the row
# @j -> Index o f the column
for i in range(file_in.shape[0]):
    row = file_in.iloc[i]
    for j in range(row.size):
        #print(row[j])
        #print(file_in.iloc[i, j])
        if row[j] == key:
            repetitions += 1
            print("##### Data finded #####\n")
            print("## Row: " + str(i) + "\n")
            print("## Column: " + str(j) + "\n")

print("\n The keyword " + key + " appears " + str(repetitions) + " times\n")