##########################
# Author: José Luis Pérez
# Date: 28/10/2020
##########################


def getKey_encrypt(pre):
    key = pre + 2
    
    return key

def getKey_desencrypt(pre):
    key = pre - 2

    return int(key)




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
        key = getKey_encrypt(ord(original[i]))
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
        key = getKey_desencrypt(ord(original[i]))
        desencrypted += chr(key)
    
    print("\n################################")
    print("##  The password desencrypted ##\n##    following the key is    ## ")
    print("################################\n\n\n")
    print("<<<< " + desencrypted + " >>>>")

    input('\nPress ENTER to exit...')
