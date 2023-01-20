numeros_pares = {2,4,6,8,10,12,14}
numeros_impares = {1,3,5,7,11,13,17}
numeros_primos = {2,3,5,7,11,13,17}
print(" ----- Interseccion de los 3 conjuntos -----")
interseccion = numeros_pares.intersection(numeros_impares, numeros_primos)
print("La intersección de los 3 conjuntos es: ", interseccion , "Es decir es vacía")
print("Cantidad de elementos de la variale interseccion: ", len(interseccion))

print()

print("--Entre los 3 conjuntos no hay interseccion, probemos de 2 en 2--")

print()

pares_impares = numeros_pares.intersection(numeros_impares)
print("La intersección de numeros pares e impares es : ", pares_impares , "Es decir es vacía")
impares_primos = numeros_impares.intersection(numeros_primos)
print("La intersección de numeros impares y primos es : ", impares_primos)
pares_primos = numeros_pares.intersection(numeros_primos)
print("La intersección de numeros pares y primos es : ", pares_primos)