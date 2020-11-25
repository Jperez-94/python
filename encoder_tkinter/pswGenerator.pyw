##########################
# Author: José Luis Pérez
# Date: 28/10/2020
##########################


from tkinter import *
import random, string


"""
Clase con los métodos necesarios para codificar y
desencriptar la información. Tiene como objetivo
simplificar y ordenar el código
"""

class Cyfer:


	# Constructor de la clase
    def __init__(self):
        self.psw = StringVar()
        self.psw_c = StringVar()
        self.length = 8
        self.letters = string.ascii_letters
        self.nums = '0123456789'
        self.spe = '-+*%&$!_'
        self.symbols = self.letters + self.nums + self.spe


    #Clave para codificar
    def getKey_encrypt(self, pre):
        key = pre + 2
        
        return key

    # Clave para descodificar
    def getKey_desencrypt(self, pre):
        key = pre - 2

        return int(key)

    # Método para generar una contraseña de longitud length
    def generatePsw(self):
        
        # @letters -> String with all the letters
        # @nums    -> String with numbers
        # @spe 	   -> String with special symbols
        # @symbols -> String with all the previous variables

        password = ''.join(random.sample(self.symbols, self.length))
        self.psw.set(password)
        self.psw_c.set(password)
        self.encrypt()


    # Método para codificar
    def encrypt(self):
        encrypted = ''
        password = self.psw_c.get()
        for i in range(len(password)):
            key = self.getKey_encrypt(ord(password[i]))
            encrypted += chr(key)
            
        self.psw_c.set(encrypted)



    # Método para descodificar
    def desencrypt(self):
        desencrypted = ''
        password = self.psw_c.get()

        for i in range(len(password)):
            key = self.getKey_desencrypt(ord(password[i]))
            desencrypted += chr(key)
        
        self.psw_c.set(desencrypted)


# Ventana del programa con sus elementos y configuración

ventana = Tk()
ventana.title("Generador de contraseñas")
ventana.geometry("400x300")
ventana.resizable(0,0)


"""
La imagen origen del icono candado_abierto se atribuye a

Freepik
www.freepik.com

Visita su pagina web para más contenido
"""

ventana.iconbitmap("./candado-abierto.ico")

# Objeto de la clase

cyfer = Cyfer()

# Contiene la contraseña generada sin cifrar

Entry(
    ventana,
    textvariable= cyfer.psw,
    font=('Arial', 20),
    justify = CENTER
).pack(pady = 15,)

# Boton para generar contraseña

Button(
    ventana,
    text = "Generar",
    font=('Arial', 15),
    command= lambda: cyfer.generatePsw()
).pack()

#Contiene la contraseña codificada o sin codificar

Entry(
    ventana,
    font=('Arial', 20),
    justify = CENTER,
    textvariable = cyfer.psw_c
).pack(pady = 5)

#Boton para codificar la contraseña

Button(
    ventana,
    text = "Cifrar",
    font=('Arial', 15),
    command = lambda: cyfer.encrypt()
).pack(anchor= CENTER, pady = 2.5)

#Boton para descodificar la contraseña

Button(
    ventana,
    text = "Descifrar",
    font=('Arial', 15),
    command = lambda: cyfer.desencrypt()
).pack(anchor= CENTER, pady = 2.5)


# Inicia la ventana

ventana.mainloop()