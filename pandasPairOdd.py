##########################
# Author: Jose Luis Perez
# Date: 29/10/2020
##########################

import pandas
import os.path
import sys

#################################################
# Basic use of the python library pandas
# It counts how many pair and odd numbers
# are in a datafile with CSV format
#################################################


# @name_in   ----> Nombre del fichero con los datos
# (we add csv or xlsx depending on the type of file we want to read from)
name_in = input('File name:\n')
name_in += ".csv"
#name_in += ".xlsx"

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

# Set to True the items which rest is equal to 0
pair = (file_in % 2) == 0

n_pair = 0
n_odd = 0

# Count the True and False items in each column
for i in range(file_in.shape[1]):
    n_pair += pair[pair == True].count()[i]
    n_odd += pair[pair != True].count()[i]


print('\n------------------------------------------------------')

print('There are ' + str(n_pair) + ' pair numbers.')
print('\nThere are ' + str(n_odd) + ' odd numbers.')

print('------------------------------------------------------')