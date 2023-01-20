numeros_pares = {2,4,6,8,10,12,14}
numeros_impares = {1,3,5,7,11,13,17}
numeros_primos = {2,3,5,7,11,13,17}
print("Diferencia simetrica de 3 conjuntos")
difsimetric_parImpar = numeros_pares.symmetric_difference(numeros_impares) #Se hizo la diferencia Simetrica primero entre par e impar
diferenciaSimetrica = difsimetric_parImpar.symmetric_difference(numeros_primos) #El resultado de la diferencia simetrica entre par e impar se diferencio con el primo
print("La diferencia simetrica de los 3 conjuntos es: ", diferenciaSimetrica)
