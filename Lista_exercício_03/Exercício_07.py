def exibir_menu():
    print("Escolha uma das opções abaixo:")
    print("1 - Eu programo em Python")
    print("2 - Eu programo em PHP")
    print("3 - Eu programo em Java")

def obter_opcao():
    while True:
        try:
            opcao = int(input("Digite o número da opção desejada: "))
            if opcao in [1, 2, 3]:
                return opcao
            else:
                print("Opção inválida. Por favor, escolha um número entre 1 e 3.")
                exibir_menu()  # Exibe o menu novamente
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def main():
    exibir_menu()
    opcao = obter_opcao()
    
    if opcao == 1:
        print("Eu estou estudando Python!")
    elif opcao == 2:
        print("Eu estou estudando PHP!")
    elif opcao == 3:
        print("Eu estou estudando Java!")

if __name__ == "__main__":
    main()
