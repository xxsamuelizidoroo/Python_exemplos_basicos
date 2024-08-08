opcao = int(input("Indique a opção desejada."))

# Seleção de opções
match opcao:
    case 1:
        print("Suporte técnico.")
    case 2:
        print("Financeiro.")
    case 3:
        print("Nossos produtos.")
    case 4:
        print("Outros assuntos.")
    case _:
        print("Opção inválida!")