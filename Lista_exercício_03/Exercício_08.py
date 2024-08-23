# Inicializa a lista com os valores de 1 a 10
numeros = list(range(1, 11))

# Filtra e exibe apenas os números pares
print("Números pares de 1 a 10:")
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
