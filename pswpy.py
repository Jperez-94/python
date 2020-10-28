##########################
# Author: José Luis Pérez
# Date: 23/10/2020
##########################



import random
import string


########################################################
### Code to generate random passwords with any length
### If you want to make an only alphanumeric password,
### you have to chamge the variable symbol to only have
### letters and nums
########################################################



# @letters -> String with all the letters
# @nums    -> String with numbers
# @spe 	   -> String with special symbols
# @symbols -> String with all the previous variables

letters = string.ascii_letters
nums = '0123456789'
spe = '-+*%&$!_'
symbols = letters + nums + spe


## Create the password by joining random characters of the symbols string
# @length -> Number of character requered for the password
def generatePws(length):
      password = ''.join(random.sample(symbols, length))
      return password


## Show in the terminal the result of the process
# @psw -> Password generated at generatePws function
def show(psw):
	print("\n##################################\n")
	print("Don't share your new password\n")
	print("##################################\n\n\n")
	print("<<<<  " + str(psw) + "  >>>>")

length = input('Password characters\'s number:\n')

try:
	length = int(length)
except:
	print("\nThe number of characters requiered is invalid")
else:
	psw = generatePws(length)
	show(psw)