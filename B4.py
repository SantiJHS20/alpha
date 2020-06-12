import B4_F1 as f1
import B4_F2 as f2


f1.mostrar_bienvenida()

#nombre, edad, estatura, sexo, pais, num_amigos

nombre = f1.obtener_nombre()

datos = f2.verificacion_usuario(nombre)
edad = datos[0]
estatura = datos[1]
sexo = datos[2]
pais = datos[3]
num_amigos = datos[4]

f2.mostrar_perfil(nombre, edad, estatura, sexo, pais, num_amigos)

opcion_de_menu = 1

while opcion_de_menu != 0:
    opcion_de_menu = f2.opcion_menu()
    if opcion_de_menu == 1:
        mensaje = f2.escribir_mensaje(nombre)
    elif opcion_de_menu == 2:
        f2.mostrar_mensaje(nombre, input("Destinario: "), input("Cuál es tu mensaje? "))
    elif opcion_de_menu == 3:
        f2.mostrar_perfil(nombre, edad, estatura, sexo, pais, num_amigos)
    elif opcion_de_menu == 4:
        nombre = f1.obtener_nombre()
        datos = f2.peticion_de_datos(nombre)
        edad = datos[0]
        estatura = datos[1]
        sexo = datos[2]
        pais = datos[3]
        num_amigos = datos[4]
    elif opcion_de_menu == 5:
        f2.cambiar_usuario(nombre)
    elif opcion_de_menu == 0:
        break

f2.guardar_datos(nombre, edad, estatura, sexo, pais, num_amigos)

print("Gracias por usar Break, vuelve pronto!!!")
print("commit 2")

