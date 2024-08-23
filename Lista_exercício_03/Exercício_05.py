# Função para validar o nome
def validar_nome(nome):
    return len(nome) > 3

# Função para validar a idade
def validar_idade(idade):
    return 0 <= idade <= 100

# Função para validar o salário
def validar_salario(salario):
    return salario > 0

# Função para validar o sexo
def validar_sexo(sexo):
    return sexo in ['f', 'm']

# Função para validar o estado civil
def validar_estado_civil(estado_civil):
    return estado_civil in ['s', 'c', 'v', 'd']

# Função para obter e validar as informações do usuário
def obter_informacoes():
    while True:
        nome = input("Digite seu nome (maior que 3 caracteres): ")
        if validar_nome(nome):
            break
        else:
            print("Nome inválido. Deve ter mais de 3 caracteres.")
    
    while True:
        try:
            idade = int(input("Digite sua idade (entre 0 e 100): "))
            if validar_idade(idade):
                break
            else:
                print("Idade inválida. Deve estar entre 0 e 100.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro para a idade.")
    
    while True:
        try:
            salario = float(input("Digite seu salário (maior que zero): "))
            if validar_salario(salario):
                break
            else:
                print("Salário inválido. Deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido para o salário.")
    
    while True:
        sexo = input("Digite seu sexo (f para feminino, m para masculino): ").lower()
        if validar_sexo(sexo):
            break
        else:
            print("Sexo inválido. Deve ser 'f' ou 'm'.")
    
    while True:
        estado_civil = input("Digite seu estado civil (s para solteiro, c para casado, v para viúvo, d para divorciado): ").lower()
        if validar_estado_civil(estado_civil):
            break
        else:
            print("Estado civil inválido. Deve ser 's', 'c', 'v' ou 'd'.")
    
    return nome, idade, salario, sexo, estado_civil

# Obtém e exibe as informações validadas
nome, idade, salario, sexo, estado_civil = obter_informacoes()
print("\nInformações do usuário:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario:.2f}")
print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
print(f"Estado Civil: {'Solteiro' if estado_civil == 's' else 'Casado' if estado_civil == 'c' else 'Viúvo' if estado_civil == 'v' else 'Divorciado'}")
