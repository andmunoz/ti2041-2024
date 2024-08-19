import math

# ENTRADA
angulo = float(input("Su ángulo (en radianes)? "))

# PROCESAMIENTO
sin_angulo = round(math.sin(angulo), 3)
cos_angulo = round(math.cos(angulo), 3)

# SALIDA
print("Los valores para el seno y el coseno:")
print(f"sin({angulo}) = {sin_angulo}")
print(f"cos({angulo}) = {cos_angulo}")
