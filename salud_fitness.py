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
    print("____________________________________________________________________________________________________")

if pasos >= META_PASOS_DIARIOS:
    print(f"Felicidades {nombre} lograste la meta de pasos diarios hiciste {pasos} pasos el dia de hoy.")
    print(f"{nombre} La distancia aproximada que recorriste hoy fue de {distancia / 100:.2f} mts")
    print(f"{nombre} La velocidad aproximada que tuviste hoy fue de {velocidad:.2f} km/h")
    print(f"{nombre} Las calorias quemadas aproximadamente es de {calorias_quemadas:.1f} calorias quemadas.")
else:
    print("____________________________________________________________________________________________________")
    print(f"{nombre} Tienes que mejorar el ritmo y la cantidad de pasos no lograste la meta diaria.")
    print(f"Hiciste {pasos} pasos el dia de hoy.")
    print(f"{nombre} La distancia aproximada que recorriste hoy fue de {distancia / 100:.2f} mts")
    print(f"{nombre} La velocidad aproximada que tuviste hoy fue de {velocidad:.2f} km/h")
    print(f"{nombre} Las calorias quemadas aproximadamente es de {calorias_quemadas:.1f} calorias quemadas.")
#__________________________________________________________________________________________________________________________________
# SEGUNDO PROGRAMA V1.1 FINALIZADO.
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

#________________________________________________________________________________________
# PROGRAMA 3 V2.0 FINALIZADO.
guion = "_"
print(guion * 90)
print("BIENVENIDO AL PROGRAMA DEL NUMERO MAYOR")
print(guion * 90)
numero1 = int(input("Indiqueme por favor un numero entero: ")) 
numero2 = int(input("Indiqueme por favor el segundo numero entero: "))
if numero1 > numero2:
    print(f"El numero mayor es: {numero1}") 
else:
    print(f"El numero mayor es el: {numero2}")
print("GRACIAS POR USAR MI PROGRAMA")
#__________________________________________________________________________________________
# PROGRAMA 4 V2.1 finalizado.
guion = "_"
print(guion * 90)
print("IDENTIFICADOR DE ESTACIONES DEL AÑO")
print(guion * 90)
mes = int(input("Indiqueme el numero del mes del 1 al 12: ").strip())

if mes < 1 or mes > 12:
    print("Este numero no corresponde a ningun mes, digite un numero de mes correcto.")
elif mes == 1 or mes == 2 or mes == 12:
    print("Se encuentra en la estación de invierno.")
elif mes == 3 or mes == 4 or mes == 5:
    print("Se encuentra en la estación de primavera.")
elif mes == 6 or mes == 7 or mes == 8:
    print("Se encuentra en la estación de verano.")
elif mes == 9 or mes == 10 or mes == 11:
    print("Se encuentra en la estación de otoño.")
else:
    print("Indique un caracter valido")
print("Gracias por usar nuestro programa.")
#_________________________________________________________________________________________________
# PROGRAMA 5 V2.2 EN PROCESO.
guion = "_"
print(guion * 90)
print("BIENVENIDOS AL PROGRMA DE SISTEMA DE CALIFICACIONES")
print(guion * 90)
calificacion = int(input("Ingresa por favor la calificación entre 0 y 10: ").strip())
if calificacion >= 9 and calificacion <= 10:
    print("Su calificación es: A ")
elif calificacion >= 8:
    print("Su calificación es: B ")
elif calificacion >= 7:
    print("Su calificación es C ")
elif calificacion >= 6:
    print("Su calificación es D ")
elif calificacion >= 0:
    print("Su calificación es F")
else:
    print("VALOR DESCONOCIDO")
print("Gracias por usar mi programa.")

#________________________________________________________________________________________________________
#   SISTEMA DE ENVIO
print("BIENVENIDOS A SERVIENTREGA ¡¡garantizamos tu entrega!!")
guion = "_"
destino = input("El destino de su paquete es (Nacional o internacional?): ").upper().strip()
peso = float(input("Indiqueme por favor el peso del paquete en kg: ").strip())
tarifa_nacional = 10000
tarifa_internacional = 20000
#________________________________
#   SISTEMA DE ENVIO
print("BIENVENIDOS A SERVIENTREGA ¡¡garantizamos tu entrega!!")
guion = "_"
print(guion * 90)
print()
destino = input("El destino de su paquete es (Nacional o internacional?): ").upper().strip()
peso = float(input("Indiqueme por favor el peso del paquete en kg: ").strip())
tarifa_nacional = 5000
tarifa_internacional = 10000
print(guion * 90)
print()
print(guion * 90)
if destino == "NACIONAL":
    costo = peso * tarifa_nacional
    print("\t\tFACTURA ELECTRONICA")
    print (f"El costo total del envio es: COP$ {costo:,.2f} Pesos colombianos.")
    print (f"El peso del envio es {peso} kg.")
    print("Gracias por confiar en servientrega")
    print()
    print(guion * 90)
elif destino == "INTERNACIONAL":
    costo = peso * tarifa_internacional
    print("\t\tFACTURA ELECTRONICA")
    print (f"El costo total del envio es COP$ {costo:,.2f} Pesos colombianos.")
    print(f"El peso de su paquete es: {peso} kg.")
    print("Gracias por confiar en servientrega")
    print()
    print(guion * 90)
else:
    print("Su Respuestas no son validas por favor vuelva a intentarlo.")
print(guion * 90)
print("GRACIAS POR ESCOGERNOS COMO SU ALIDO PUEDE COMUNICARSE CON NOSOTROS POR LA LINEA: 909191401")
print(guion * 90)
#_____________________________________________________________________________________________________
# SISTEMA DE AUTENTICACION 
guion = "_"
print(guion * 90)
print("BIENVENIDOS AL SISTEMA DE AUTENTICACIÓN DE USUARIO DE POSITIVA.")
print(guion * 90)
print()
USUARIO = "bdelarosa"
PASSWORD = "12345678"
user = input("Por favor ingrese su nombre de usuario: ").strip()
contrasena = input("Ingrese su contraseña: ").strip()
if USUARIO == user and PASSWORD == contrasena:
    print(guion * 90)
    print()
    print("BIENVENIDOS A LA BASE DE DATOS DE POSITIVA")
    print(guion * 90)
    print("Gracias por usar positiva compañia de seguros.")
elif USUARIO != user:
    print()
    print(guion * 90)
    print("Usuario invalido.")
elif PASSWORD != contrasena:
    print("Contraseña invalida.")
else:
    print("Usuario y contraseña invalidos.")
print()
print("Gracias por hacercarse mas a positiva compañia de seguros!!")


