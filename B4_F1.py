
def mostrar_bienvenida():
    print("Bienvenido a ... ")
    print("""
    ______                _    
    | ___ \              | |   
    | |_/ /_ __ ___  __ _| | __
    | ___ \ '__/ _ \/ _` | |/ /
    | |_/ / | |  __/ (_| |   < 
    \____/|_|  \___|\__,_|_|\_\    

    """)

def obtener_nombre():
    nombre = input("Para empezar, dime como te llamas. ")
    return nombre

def obtener_edad():
    agno = int(input("Para preparar tu perfil, dime en que año naciste. "))
    edad = 2020 - agno - 1
    return edad

def obtener_estatura():
    estatura = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
    return estatura

def obtener_sexo():
    sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    while sexo != 'M' and sexo != 'F':
        sexo = input("Por favor, ingresa tu sexo (M=Masculino, F=Femenino): ")
    return sexo

def obtener_pais():
    pais = input("Indica tu país de origen ;) ")
    return pais

def obtener_num_amigos():
    amigos = int(input("Muy bien. Finalmente, cuÃ©ntame cuantos amigos tienes. "))
    return amigos








