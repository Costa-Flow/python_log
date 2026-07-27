# 1. Definición de Variables (Parámetros)
medida_nominal = 10.00
tolerancia = 0.05
medida_real = 10.01  # Lectura de muestra

# 2. Cálculo de Límites
limite_inferior = medida_nominal - tolerancia  # 9.95
limite_superior = medida_nominal + tolerancia  # 10.05

# 3. Lógica de Control (Toma de Decisiones)
if limite_inferior <= medida_real <= limite_superior:
    print("STATUS: Pieza ACEPTADA (Dentro de tolerancia)")
else:
    print("STATUS: Pieza RECHAZADA (Fuera de especificación)")
    