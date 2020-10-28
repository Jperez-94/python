##########################
# Author: José Luis Pérez
# Date: 28/10/2020
##########################


############################################################
# Takes the equivalent of each character in the ASCII table
# and add 2 to its value. Finally it reverts the number to
# the equivalent character following the same table
############################################################
#
# @original -> Word to be encrypted

def encrypt(original):
    encrypted = ''

    for i in range(len(original)):
        pre = ord(original[i])
        key = pre + 2
        encrypted += chr(key)

    print("\n#############################")
    print("##  The password encrypted ##\n##   following the key is  ## ")
    print("#############################\n\n\n")
    print("<<<< " + encrypted + " >>>>")

    input('\nPress ENTER to exit...')


############################################################
# Takes the equivalent of each character in the ASCII table
# and subtract 2 to its value. Finally it reverts the number to
# the equivalent character following the same table
############################################################
#
# @original -> Word to be desencrypted

def desencrypt(original):
    desencrypted = ''

    for i in range(len(original)):
        pre = ord(original[i])
        key = pre - 2
        desencrypted += chr(key)
    
    print("\n################################")
    print("##  The password desencrypted ##\n##    following the key is    ## ")
    print("################################\n\n\n")
    print("<<<< " + desencrypted + " >>>>")

    input('\nPress ENTER to exit...')