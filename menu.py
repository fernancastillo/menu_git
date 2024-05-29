import os
import msvcrt
import time
usuarios=[]
os.system("cls")
print("Bienvenido al menú.")
while True:
    print("Presione una tecla para continuar.")
    msvcrt.getch()
    print("Menú")
    print("1. Inicio sesión.")
    print("2. Registrar usuario.")
    print("3. Eliminar usuario.")
    print("4. Salir.")
    opc=int(input("Ingrese el número del menú: "))
    if opc==1:
        pass
    elif opc==2:
        print("REGISTRAR USUARIO")
        nombre=input("Ingrese su nombre de usuario: ")
        contra=input("Ingrese su contraseña: ")
        usuario={
            "nombre":nombre,
            "contra":contra
        }
        usuarios.append(usuario)
        print("Usuario agregado con éxito!")
    elif opc==3:
        print("ELIMINAR USUARIO")
        nombre=input("Ingrese el nombre de usuario: ")
        for x in range (len(usuarios)):
            if nombre==usuarios[x]["nombre"]:
                contra=input("Ingrese la contraseña: ")
                if contra==usuarios[x]["contra"]:
                    usuarios.pop(x)
                    print("Usuario eliminado con éxito!")
                else:
                    print("Contraseña incorrecta!")
            else:
                print("Usuario no registrado!")
    else:   
        break