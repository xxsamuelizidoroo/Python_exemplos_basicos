# Função para obter um número válido do usuário
def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

# Obtém dois números do usuário
numero1 = obter_numero("Digite o primeiro número: ")
numero2 = obter_numero("Digite o segundo número: ")

# Realiza 3 somas
soma1 = numero1 + numero2
soma2 = numero1 + numero2
soma3 = numero1 + numero2

# Calcula o totalizador
totalizador = soma1 + soma2 + soma3

# Exibe os resultados
print(f"\nResultado das somas:")
print(f"Soma 1: {soma1}")
print(f"Soma 2: {soma2}")
print(f"Soma 3: {soma3}")
print(f"\nTotalizador das somas: {totalizador}")
