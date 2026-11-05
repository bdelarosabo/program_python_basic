# PRIMER PROGRAMA V1.0 FINALIZADO EXITOSAMENTE.
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
#__________________________________________________________________________________________________________________________________
# SEGUNDO PROGRAMA V1.1 EN PROCESO.
guion = "_"
print(guion * 90)
print("SISTEMA DE RESERVA DE HOTEL")
print(guion * 90)
nombre = input("Indiqueme por su nombre: ").strip()
dias = int(input("Indiqueme por favor los dias de estadia en el hotel: ").strip())
cuarto = input("Desea la habitacion con vista al mar (SI/NO): ").strip().upper()
ingreso = input("Indiqueme la fecha de llegada al hotel: ").strip()
salida = input("Indiqueme la fecha de salida del hotel: ").strip()
print(guion * 90)
print()
habitacion_sin_vista = 150.50
habitacion_con_vista = 190.50
print(guion * 90)
print("RESULTADO DE LA RESERVA")
print(guion * 90)

if dias <= 0:
    print("No ingreso un numero correcto el la pregunta de sus dias de estadia, vuelva a intentarlo por favor. ")
elif cuarto == "SI":
    reserva = dias * habitacion_con_vista
    print(f"Gracias por su reserva señor {nombre}, su habitación es con vista al mar.")
    print(f"Su fecha de ingreso al hotel queda reservada para el {ingreso} y su fecha de salida es el {salida}.\nCon una duración de {dias} dias calendario.")
    print(f"El monto a pagar por la reserva es de {reserva}")
elif cuarto == "NO":
    reserva = dias * habitacion_sin_vista
    print(f"Gracias por su reserva señor {nombre}, su habitación es sin vista al mar.")
    print(f"Su fecha de ingreso al hotel queda reservada para el {ingreso} y su fecha de salida es el {salida}.\nCon una duración de {dias} dias calendario.")
    print(f"El monto a pagar por la reserva es de {reserva}")
else:
    print('La respuesta ingresada es erronea, ingrese correctamente si desea un cuarto con vista al mar o no responda "SI" o "NO".')
print("Gracias por usar nuestro programa.")

