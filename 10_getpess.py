# Importação de biblioteca getpass
import getpass as gtp

usuario = input("Nome do usuário: ")  
senha = gtp.getpass("Digite sua senha: ")  

# Verificação do número de caracteres da senha
if len(senha) <= 8:  
    print("Usuário cadastrado com sucesso!")  
else:
    print("Atenção! A senha deve ter no máximo 6 dígitos!") 