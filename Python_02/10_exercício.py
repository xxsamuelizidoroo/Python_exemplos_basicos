# Exibindo título
print("===== LOJAS =====")
print(" ")

# Array das lojas 
lojas = {"Santo André", "São Bernardo", "São Caetano", "Diadema"}

# Exibindo lojas com numeração
for i, loja in enumerate(lojas, 1):
    print(f"{i}. {loja}")
    print(" ")

# Escolhendo uma loja para exibir
loja_selecionada = int(input("Selecione a loja desejada."))

# Exibindo a loja selecionada (Caso revista)
if 1 <= loja_selecionada <= len(lojas):
    print(lojas(loja(loja_selecionada -1)))
else:
    print("Loja inválida")
    
