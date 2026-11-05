guion = "_"
print(guion * 90)
print("BIENVENIDO A MI PROGRAMA DE SALUD Y FITNESS")
print(guion * 90)
print()

META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASOS = 0.04  

nombre = input("Por favor ingrese su nombre de usuario: ").strip()
pasos = int(input("Indiqueme los pasos caminados en el dia: ").strip())
estatura = float(input("Indiqueme por favor su estatura en centimetros (ej 170): ").strip())
tiempo_caminado = float(input("Cuanto tiempo en minutos camino?: ").strip())

calorias_quemadas = pasos * CALORIAS_POR_PASOS
zancada = estatura * 0.0415
distancia = pasos * zancada
if tiempo_caminado > 0:
    velocidad = (distancia / 100000) / (tiempo_caminado / 60)   # km/h
else:
    velocidad = 0

if pasos >= META_PASOS_DIARIOS:
    print(f"Felicidades {nombre} lograste la meta de pasos diarios hiciste {pasos} pasos el dia de hoy.")
    print(f"{nombre} La distancia aproximada que recorriste hoy fue de {distancia / 100:.2f} mts")
    print(f"{nombre} La velocidad aproximada que tuviste hoy fue de {velocidad:.2f} km/h")
    print(f"{nombre} Las calorias quemadas aproximadamente es de {calorias_quemadas:.1f} calorias quemadas.")
else:
    print(f"{nombre} Tienes que mejorar el ritmo y la cantidad de pasos no lograste la meta diaria.")
