print("Bienvenido al Programa Jalisco")

jugar = "SI"
while jugar != "NO":
    # ENTRADA
    numero = None
    try:
        numero = int(input("Ingresa un número? "))
    except ValueError:
        print("¡Tienes que ingresar un número!")

    # PROCESAMIENTO
    if numero != None and numero >= 1 and numero <= 100:
        respuesta = numero + 1
        print(f"Ja ja ja, te gané con el {respuesta}")
    elif numero != None:
        print("Eres un tramposo, te dije entre 1 y 100")
        
    jugar = input("Quieres seguir jugando? ").upper()

# SALIDA
print("¡Hasta la Próxima!")
