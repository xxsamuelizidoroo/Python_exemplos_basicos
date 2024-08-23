# Cabeçalho da tabela
print(f"{'Nro':<5}\t{'Quad':<10}\t{'Cubo':<10}")

# Calcula e exibe os quadrados e cubos dos números de 0 a 50
for nro in range(51):
    quad = nro ** 2
    cubo = nro ** 3
    print(f"{nro:<5}\t{quad:<10}\t{cubo:<10}")
