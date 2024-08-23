# Função para validar nota
def validar_nota(nota):
    return 0 <= nota <= 10

# Lista para armazenar as notas
notas = []

# Solicita 4 notas ao usuário
for i in range (1, 5):
    try:
        nota = float(input(f"Digite a nota {i}: "))
        if validar_nota(nota):
            notas.append(nota)
        else:
            print("Nota inválida. Insira um valor entre 0 e 10.")
            break
    except ValueError:
        print("Entrada inválida. Insira um número váalido")
        break
else:
    media = sum(notas) / len(notas)
    print(f"A média das notas é: {media:.2f}")

     