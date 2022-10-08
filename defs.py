import validacoes
from os import system
from time import sleep


def limpar_tela():
    sleep(1)
    system('cls') or None


def menu():
    limpar_tela()
    print("""
*******Python Bank******
Escolha a opção desejada
1 - Cadastrar Usuário 
2 - Login
3 - Sair
************************
""")
    escolha = int(input("Digite a opção desejada: "))
    while escolha < 1 or escolha > 3:
        print("Digite uma opção válida!")
        escolha = int(input("Digite a opção desejada: "))
    limpar_tela()
    return escolha


def cadastro_usuario(cpf, nome, data_nascimento, endereco, clientes):

    usuario_cadastrado = list()
    informacoes = list()

    cpf = validacoes.valida_cpf(cpf)
    validacoes.cliente_unico(cpf, clientes)
    nome = validacoes.valida_nome(nome)
    data_nascimento = validacoes.valida_nascimento(data_nascimento)
    endereco = validacoes.valida_endereco(endereco)
    informacoes.append(nome)
    informacoes.append(data_nascimento)
    informacoes.append(endereco)
    usuario_cadastrado.append(cpf)
    usuario_cadastrado.append(informacoes)
    return usuario_cadastrado


def clientes_banco(clientes):

    quantidade_clientes = 0
    login_cliente = 0
    print("""
*******Python Bank******
Clientes cadastrados: """)
    for user in clientes:
        quantidade_clientes += 1
        print(f"{quantidade_clientes} - {user[1][0]} - {user[0]}")

    print("""************************""")
    while not login_cliente:
        login_cliente = input("Digite a opção desejada: ")
        if not login_cliente.isnumeric():
            print("Digite o número de sua opção.")
            login_cliente = 0
        else:
            login_cliente = int(login_cliente)
            if login_cliente > quantidade_clientes or login_cliente <= 0:
                print("Digite um valor válido.")

    return login_cliente - 1

