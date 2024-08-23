# Coletar valor a ser convertido
dolar = float(input("Informe o valor em dolar USD: "))

# 1USD vale 0,92EUR (Cotação de 02/08/2024)
cot_euro = 0.92

# Conversão USD para EUR
conversao = dolar * cot_euro

# Exibir o valor convertido
print("O valor convertido é de: {:.2f} EUR.".format(conversao))