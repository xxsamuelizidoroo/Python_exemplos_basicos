def sabor_pizza(sabor):
    match sabor:
        case 1: 
            return "Mussarela"
        case 2: 
            return "Calabresa"
        case 3: 
            return "Frango c/ catupiry"
        case 4: 
            return "Portuguesa"
        case _:
            return "Sabor inválido"

# Solicita a opção desejada 
sabor = int(input("Indique a opção desejada (1 para Mussarela, 2 para Calabresa, etc.): "))

# Exibe o resultado da função na tela
print(sabor_pizza(sabor))
