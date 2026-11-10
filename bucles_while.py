# REALIZA LA SUMA DE LOS PRIMEROS 5 NUMEROS UTILIZANDO UN CICLO WHILE:
# 1 + 2 + 3 + 4 + 5 = 15
#   3   + 3 
#       6   + 4
#           10  + 5
#               15  = RESULTADO ESPERADO.
# _______________________________________________________________________ 
contador = 1
suma = 0

while contador <= 5:
    suma = suma + contador
    contador = contador + 1

print("La suma de los primeros 5 números es:", suma)
#________________________________________________________________________
