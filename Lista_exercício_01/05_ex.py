
# Coletar valores
v_produto = float(input("Informe o valor do produto: "))
perc_comissao = float(input("Informe o percentual da comissão: "))

# Efetuar cálculos
comissao = (v_produto * (perc_comissao / 100))

# Exibir valor da comissão
print(f"O valor da comissão é de R$ {comissao}.")
