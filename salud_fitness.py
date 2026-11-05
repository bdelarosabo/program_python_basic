guion = "_"
print(guion * 90)
print("BIENVENIDO A MI PROGRAMA DE SALUD Y FITNESS")
print(guion * 90)
print()

META_PASOS_DIARIOS = 10,000
CALORIAS_POR_PASOS = 0,04  # valor aprox en kilometro x calorias.

nombre = input("Por favor ingrese su nombre de usuario: ").strip()
pasos = int(input("Indiqueme los pasos caminados en el dia: ").strip())
peso = float(input("Indiqueme su peso actual: ").split())
estatura = float(input("Indiqueme por favor su estatura: ").strip())
tiempo_caminado = float(input("Cuanto tiempo en minutos camino?: ").strip())

calorias_quemadas = pasos * CALORIAS_POR_PASOS
zancada = 0,0415 * estatura
distancia = pasos * zancada
velocidad = distancia / tiempo_caminado

