import B4_F1 as f1
import os

def peticion_de_datos(nombre):
    print("Hola ", nombre, ", bienvenido a Break")
    edad = f1.obtener_edad()
    estatura = f1.obtener_estatura()
    sexo = f1.obtener_sexo()
    pais = f1.obtener_pais()
    num_amigos = f1.obtener_num_amigos()
    return edad, estatura, sexo, pais, num_amigos

def mostrar_perfil(nombre, edad, estatura, sexo, pais, num_amigos):
    print("--------------------------------------------------")
    print("Nombre:   ", nombre)
    print("Edad:     ", edad, "aÃ±os")
    print("Estatura: ", estatura)
    print("Sexo:     ", sexo)
    print("PaÃ­s:    ", pais)
    print("Amigos:   ", num_amigos)
    print("--------------------------------------------------")

def opcion_menu():
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje pÃºblico")
    print("  2. Escribir un mensaje solo a algunos amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  5. Cambiar de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opciÃ³n: "))
    while opcion < 0 or opcion > 5:
        print("No conozco la opciÃ³n que has ingresado. IntÃ©ntalo otra vez.")
        opcion = int(input("Ingresa una opciÃ³n: "))
    return opcion

def escribir_mensaje(nombre):
    mensaje = input("Vamos a publicar un mensaje. ¿Qué piensas hoy? ")
    print()
    print("--------------------------------------------------")
    print(nombre, "dice:", mensaje)
    print("--------------------------------------------------")

def mostrar_mensaje(origen, destinatario, mensaje):
    print("--------------------------------------------------")
    if destinatario == None:
        print(origen, "dice:", mensaje)
    else:
        print(origen, "dice:", "@"+destinatario, mensaje)
    print("--------------------------------------------------")

def guardar_datos(nombre, edad, estatura, sexo, pais, num_amigos):
    archivo = open(nombre+".user", "w")
    archivo.write(nombre + "\n")
    archivo.write(str(edad) + "\n")
    archivo.write(str(estatura) + "\n")
    archivo.write(sexo + "\n")
    archivo.write(pais + "\n")
    archivo.write(str(num_amigos) + "\n")
    archivo.close()

def verificacion_usuario(nombre):
    if os.path.isfile(nombre + ".user"):
        print("Leyendo datos de usuario", nombre, "desde archivo.")
        archivo_usuario = open(nombre + ".user", "r")
        nombre = archivo_usuario.readline().rstrip()
        edad = int(archivo_usuario.readline().replace("\n", ""))
        estatura = float(archivo_usuario.readline().replace("\n", ""))
        sexo = archivo_usuario.readline().replace("\n", "")
        pais = archivo_usuario.readline().rstrip()
        num_amigos = int(archivo_usuario.readline().replace("\n", ""))
        archivo_usuario.close()

    else:
        datos = peticion_de_datos(nombre)
        edad = datos[0]
        estatura = datos[1]
        sexo = datos[2]
        pais = datos[3]
        num_amigos = datos[4]

    return edad, estatura, sexo, pais, num_amigos


def red_social_accionar(nombre):

    datos = verificacion_usuario(nombre)
    edad = datos[0]
    estatura = datos[1]
    sexo = datos[2]
    pais = datos[3]
    num_amigos = datos[4]

    mostrar_perfil(nombre, edad, estatura, sexo, pais, num_amigos)

    opcion_de_menu = 1

    while opcion_de_menu != 0:
        opcion_de_menu = opcion_menu()
        if opcion_de_menu == 1:
            mensaje = escribir_mensaje(nombre)
        elif opcion_de_menu == 2:
            mostrar_mensaje(nombre, input("Destinario: "), input("Cuál es tu mensaje? "))
        elif opcion_de_menu == 3:
            mostrar_perfil(nombre, edad, estatura, sexo, pais, num_amigos)
        elif opcion_de_menu == 4:
            nombre = f1.obtener_nombre()
            datos = peticion_de_datos(nombre)
            edad = datos[0]
            estatura = datos[1]
            sexo = datos[2]
            pais = datos[3]
            num_amigos = datos[4]
        elif opcion_de_menu == 5:
            cambiar_usuario(nombre)
        elif opcion_de_menu == 0:
            break

    guardar_datos(nombre, edad, estatura, sexo, pais, num_amigos)

    print("Gracias por usar Break, vuelve pronto!!!")


def cambiar_usuario(nombre):
    nombre = input("Nombre del usuario al que deseas ingresar: ")
    if os.path.isfile(nombre + ".user"):
        red_social_accionar(nombre)
    else:
        print("No puedes cambiar a este usuario, porque no existe.")