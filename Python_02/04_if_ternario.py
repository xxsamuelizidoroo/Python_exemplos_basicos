velocidade = int(input("Informe as velocidades: "))

# Uso do if ternário
alerta = "Alta velocidade! Multado." if velocidade > 60 else "Dentro do limite de velocidade."

# Exibição
print(alerta)