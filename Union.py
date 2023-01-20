numeros_pares = {2,4,6,8,10,12,14}
numeros_impares = {1,3,5,7,11,13,17}
numeros_primos = {2,3,5,7,11,13,17}

print("-- Unión de los 3 conjuntos --")

union = numeros_pares.union(numeros_impares,numeros_primos)
print("La unión de los 3 conjuntos es: ", union)