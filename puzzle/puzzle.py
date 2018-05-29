from tkinter import *
from tkinter import ttk, font
import json
import os
import pygame
import sys
import random
from pygame.locals import *

fal = bool(0)
ver = bool(1)
a = []
b = []
using = ""
usuario1 = ""
user = ""
passw = ""
inicio_sesion = False

def iniciar_sesion():
    global inicio_sesion, user, passw

    user = Campo0.get()
    passw = Campo1.get()

    etiq2.configure(text="iniciando")

    with open("users.json") as lista:
        usuarios = json.load(lista)
        print(usuarios)
        for usuario in usuarios:
            print(usuario.get("user"))
            if usuario.get("user") == user:
                print(usuario.get("password"))
                if usuario.get("password") == passw:
                    print("Autenticado")
                    etiq2.configure(text="Confirmado")
                    inicio_sesion = True
                    break
        if not inicio_sesion:
            etiq2.configure(text="Usuario no registrado")


def registrar():
    global inicio_sesion, user, passw

    user = Campo0.get()
    passw = Campo1.get()
    verificar_nickname()
    verificar_clave()

    with open('users.json', 'r') as lista:
        usuarios = json.load(lista)
        nuevo_user = {}
        nuevo_user["user"]=user
        nuevo_user["password"]=passw
        print(nuevo_user)
        usuarios.append(nuevo_user)
        lista.close()

    os.remove('users.json')
    with open('users.json', 'w') as lista:
        json.dump(usuarios,lista, indent=4)
        lista.close()
    etiq2.configure(text="Registrado.")
    Campo0.delete(0,"end")
    Campo1.delete(0,"end")


def verificar_nickname():
    if len(a) > 0:
        a.pop(0)
    nombre_usuario = user
    long = len(nombre_usuario)  # Calcular la longitud del nomre de usuario
    y = nombre_usuario.isalnum()  # Calcula que la cadena contenga valores alfanuméricos

    if y == False:  # La cadena contiene valores no alfanuméricos
        print("El nombre de usuario puede contener solo letras y números")
    if long < 6:
        print("El nombre de usuario debe contener al menos 6 caracteres")
        print(nombre_usuario)
    if long > 12:
        print("El nombre de usuario no puede contener más de 12 caracteres")
        print(nombre_usuario)
    if long > 5 and long < 13 and y == True:
        #using = usuario.get()
        #texto = "Hola " + nombre_usuario
        #usuario.set(texto)
        #a.append(1)
        return ver  # Verdadero si el tamaño es mayor a 5 y menor a 13


def verificar_clave():
    if len(b) > 0:
        b.pop(0)
    contraseña_usuario = passw
    validar = False  # que se vayan cumpliendo los requisitos uno a uno.
    long = len(contraseña_usuario)  # Calcula la longitud de la contraseña
    espacio = False  # variable para identificar espacios
    mayuscula = False  # variable para identificar letras mayúsculas
    minuscula = False  # variable para contar identificar letras minúsculas
    numeros = False  # variable para identificar números
    y = contraseña_usuario.isalnum()  # si es alfanumérica retona True
    correcto = True  # verifica que hayan mayuscula, minuscula, numeros y no alfanuméricos

    for carac in contraseña_usuario:  # ciclo for que recorre caracter por caracter en la contraseña

        if carac.isspace() == True:  # Saber si el caracter es un espacio
            espacio = True  # si encuentra un espacio se cambia el valor user

        if carac.isdigit() == True:  # saber si hay números
            numeros = True  # acumulador o contador de numeros

    if espacio == True:  # hay espacios en blanco
        print("La contraseña no puede contener espacios")
    else:
        validar = True  # se cumple el primer requisito que no hayan espacios

    if long < 6 and validar == True:
        print("Mínimo 6 caracteres")
        validar = False  # cambia a Flase si no se cumple el requisito móinimo de caracteres

    if numeros == True and validar == True:
        validar = True  # Cumple el requisito de tener numeros y no alfanuméricos
    else:
        correcto = False  # uno o mas requisitos de mayuscula, minuscula, numeros y no alfanuméricos no se cumple

    if validar == True and correcto == False:
        print("La contraseña elegida no es segura: debe contener letras y números")

    if validar == True and correcto == True:
        print("felicidades")
        b.append(1)
        return True


def confirmacion():
    user = usuario.get()
    user2 = usuario1.get()
    # print(user)
    # print(user2)
    comparar(user, user2)


def comparar(txt, txt1):
    if len(txt) == len(txt1):
        for i in range((len(txt)) - 1):
            if txt[i] == txt1[i]:
                print("bn")
            else:
                print("mal")
    else:
        print("contraseña incorrecta ")


def ventana():
    clave()
    if len(a) == 1 and len(b) == 1:
        # raiz1 = tkinter.Toplevel(raiz)
        # raiz.iconify()
        # using=usuario.get()
        raiz.destroy()
        raiz1 = Tk()
        raiz1.geometry('595x160')
        raiz1.configure(bg='red')
        raiz1.title('confirmar')

        fuente = font.Font(weight='bold')

        usuario1 = StringVar()
        contraseña1 = StringVar()

        marco1 = ttk.Frame(raiz1, borderwidth=5, relief="ridge", padding=(95, 5))
        botonJ = ttk.Button(marco1, text="INGRESAR", padding=(4, 4), command=confirmacion)
        botonB = ttk.Button(marco1, text="ACEPTAR", padding=(2, 5), command=ventana)
        Campo2 = ttk.Entry(marco1, textvariable=usuario1, width=25)
        Campo3 = ttk.Entry(marco1, textvariable=contraseña1, width=25)
        etiq2 = ttk.Label(marco1, text="Confirmar Usuario ", font=fuente, padding=(10, 5))
        etiq3 = ttk.Label(marco1, text="Confirmar Contraseña ", font=fuente, padding=(10, 5))

        botonJ.grid(row=2, column=0, columnspan=2)
        botonB.grid(row=2, column=3, columnspan=2)
        marco1.grid(row=0, column=0, padx=10, pady=20, sticky=(N, S, E, W))
        Campo2.grid(row=1, column=0, columnspan=2)
        Campo3.grid(row=1, column=4, columnspan=2)
        etiq2.grid(row=0, column=0, padx=0, pady=0, sticky=(N, S, E, W))
        etiq3.grid(row=0, column=4, padx=5, pady=0, sticky=(N, S, E, W))


# ventana.......................................................................

raiz = Tk()
raiz.geometry('700x170')
raiz.configure(bg='red')
raiz.title('registro')

fuente = font.Font(weight='bold')

valor = StringVar()
var = IntVar()

marco = ttk.Frame(raiz, borderwidth=5, relief="ridge", padding=(110, 5))
botonI = ttk.Button(marco, text="REGISTRAR", padding=(4, 4), command=registrar)
botonA = ttk.Button(marco, text="INICIAR", padding=(2, 5), command=iniciar_sesion)
etiq0 = ttk.Label(marco, text="Nombre de Usuario ", font=fuente, padding=(10, 5))
etiq1 = ttk.Label(marco, text="Contraseña ", font=fuente, padding=(10, 5))
etiq2 = ttk.Label(marco, text="", font=fuente, padding=(10, 5))
Campo0 = ttk.Entry(marco, textvariable=user, width=25)
Campo1 = ttk.Entry(marco, textvariable=passw, width=25, show='*')

botonI.grid(row=2, column=0, columnspan=2)
botonA.grid(row=2, column=3, columnspan=2)
marco.grid(row=0, column=0, padx=10, pady=20, sticky=(N, S, E, W))
Campo0.grid(row=1, column=0, columnspan=2)
Campo1.grid(row=1, column=4, columnspan=2)
etiq0.grid(row=0, column=0, padx=0, pady=0, sticky=(N, S, E, W))
etiq1.grid(row=0, column=4, padx=0, pady=0, sticky=(N, S, E, W))
etiq2.grid(row=3, column=3, padx=0, pady=0, sticky=(N, S, E, W))

raiz.mainloop()
