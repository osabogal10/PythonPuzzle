import json
import os


user=input("ususario")
passw=input("clave")
inicio_sesion = False

def sign_in():
    global inicio_sesion
    with open("users.json") as lista:
        usuarios = json.load(lista)
        print(usuarios)
        for usuario in usuarios:
            print(usuario.get("user"))
            if usuario.get("user") == user:
                print(usuario.get("password"))
                if usuario.get("password") == passw:
                    print("Autenticado")
                    inicio_sesion = True
                    break
        if not inicio_sesion:
            with open('users.json', 'r') as lista:
                usuarios = json.load(lista)
                nuevo_user = {}
                nuevo_user["user"] = user
                nuevo_user["password"] = passw
                print(nuevo_user)
                usuarios.append(nuevo_user)
                lista.close()

            os.remove('users.json')
            with open('users.json', 'w') as lista:
                json.dump(usuarios, lista, indent=4)
                lista.close()
            print("Registrado")
            inicio_sesion=True

def registrar():
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

#registrar()

def iniciar_sesion():
    jsonloads = json.loads(open('users.json').read())  # Load the json
    print(jsonloads['Usernames'][0]['pass'])
    # user = input("Enter your username: ") #Get username as a string
    for i in range(len(jsonloads['Usernames'])):  # Iterate through usernames
        print(i)
        print(passw)
        if jsonloads['Usernames'][i]['user'] == user:  # If the username is what they entered
            print("user")
            # passw = input("New password: ") #Ask for new password
            if jsonloads['Usernames'][i]['pass'] == passw:
                # jsonFile = open("users.json", "w+") #Open the json
                # jsonFile.write(json.dumps(jsonloads, indent=4)) #Write
                # jsonFile.close() #Close it
                print("iniciado")
                break  # Break out of the for loop
    # else:
    # registrar_usuario()