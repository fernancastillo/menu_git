import os
import msvcrt
import time
usuarios=[]
os.system("cls")
print("Bienvenido al menú.")
while True:
    print("Presione una tecla para continuar.")
    msvcrt.getch()
    os.system("cls")
    print("Menú")
    print("1. Inicio sesión.")
    print("2. Registrar usuario.")
    print("3. Eliminar usuario.")
    print("4. Salir.")
    while True:
        try:
            opc=int(input("Ingrese el número del menú: "))
            if opc in (1,2,3,4):
                break
            else:
                print("Error! Debe ingresar un número del 1 al 4!")
        except:
            print("Error! Debe ingresar un número entero!")
    if opc==1:
        while True:
            nombre=input("Ingrese su nombre de usuario: ")
            if len(nombre)>=3:
                break
            else:
                print("Error! Debe ingresar mínimo 3 caracteres!")
        while True:
            contra=input("Ingrese la contraseña: ")
            if len(contra)>=3:
                break
            else:
                print("Error! Debe ingresar mínimo 3 caracteres!")
        for x in range (len(usuarios)):
            if nombre==usuarios[x]["nombre"] and contra==usuarios[x]["contra"]:
                print("Sesión iniciada con éxito!")
            else:
                print("Usuario o contraseña incorrectos!")
    elif opc==2:
        print("REGISTRAR USUARIO")
        while True:
            nombre=input("Ingrese su nombre de usuario: ")
            if len(nombre)>=3:
                break
            else:
                print("Error! Debe ingresar mínimo 3 caracteres!")
        while True:
            contra=input("Ingrese la contraseña: ")
            if len(contra)>=3:
                break
            else:
                print("Error! Debe ingresar mínimo 3 caracteres!")
        usuario={
            "nombre":nombre,
            "contra":contra
        }
        usuarios.append(usuario)
        print("Usuario agregado con éxito!")
    elif opc==3:
        print("ELIMINAR USUARIO")
        while True:
            nombre=input("Ingrese su nombre de usuario: ")
            if len(nombre)>=3:
                break
            else:
                print("Error! Debe ingresar mínimo 3 caracteres!")
        for x in range (len(usuarios)):
            if nombre==usuarios[x]["nombre"]:
                while True:
                    contra=input("Ingrese la contraseña: ")
                    if len(contra)>=3:
                        break
                    else:
                        print("Error! Debe ingresar mínimo 3 caracteres!")
                if contra==usuarios[x]["contra"]:
                    usuarios.pop(x)
                    print("Usuario eliminado con éxito!")
                else:
                    print("Contraseña incorrecta!")
            else:
                print("Usuario no registrado!")
    else:
        print("Hasta la próxima!")   
        break