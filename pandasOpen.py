
##########################
# Author: Jose Luis Perez
# Date: 23/10/2020
##########################

import pandas
import os.path
import sys

#################################################
# Basic use of the python library pandas
# It only read the file and save the information
# as a DataFrame
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
#file_in = pandas.read_excel(name_in)

# Now we can extract and manipulate information of our original file without modifieing it
## For example, we can show on screen the header of each column
headers = file_in.columns

print(headers)