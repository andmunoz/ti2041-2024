dividendo = int(input("Ingrese el dividendo? "))
divisor = int(input("Ingrese el divisor? "))
try:
    cociente = dividendo // divisor
    resto = dividendo % divisor
    print(f"El cociente de {dividendo} : {divisor} es {cociente}")
    print(f"El resto de {dividendo} : {divisor} es {resto}")
except ZeroDivisionError: 
    print("No se puede dividir por 0")
except: 
    print("Ha ocurrido un error desconocido")
finally:
    print("¡Programa terminado!")
