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
0 - Sair
************************
""")
    escolha = int(input("Digite a opção desejada: "))
    while escolha < 0 or escolha > 2:
        print("Digite uma opção válida!")
        escolha = int(input("Digite a opção desejada: "))
    limpar_tela()

    return escolha


def cadastro_usuario(cpf, nome, data_nascimento, endereco, clientes):
    usuario_cadastrado = list()
    informacoes = list()

    cpf = validacoes.valida_cpf(cpf)
    validacao = validacoes.cliente_unico(cpf, clientes)
    if not validacao:
        return None
    nome = validacoes.valida_nome(nome)
    data_nascimento = validacoes.valida_nascimento(data_nascimento)
    endereco = validacoes.valida_endereco(endereco)
    informacoes.append(nome)
    informacoes.append(data_nascimento)
    informacoes.append(endereco)
    usuario_cadastrado.append(cpf)
    usuario_cadastrado.append(informacoes)
    return usuario_cadastrado


def login_cliente(clientes):

    quantidade_clientes = 0
    escolha_cliente = 0
    print("""
*******Python Bank******
Clientes cadastrados: """)
    for user in clientes:
        quantidade_clientes += 1
        print(f"{quantidade_clientes} - {user[1][0]} - {user[0]}")

    print("""0 - Sair
    ************************""")
    while not escolha_cliente:
        escolha_cliente = input("Digite a opção desejada: ")
        if not escolha_cliente.isnumeric():
            print("Digite apenas o número de sua opção.")
            escolha_cliente = 0

        else:
            escolha_cliente = int(escolha_cliente)
            if escolha_cliente == 0:
                break
            elif escolha_cliente > quantidade_clientes or escolha_cliente < 0:
                print("Digite um valor válido.")

    return escolha_cliente - 1


def menu_cliente_logged(cliente_logado):
    escolha = 0
    while not escolha:
        limpar_tela()
        print(f"""
*******Python Bank******
Bem-vindo(a)
{cliente_logado[1][0]} - {cliente_logado[0]}
Escolha a opção desejada
1 - Criar Conta Bancária
2 - Administrar Conta
0 - Sair
************************
        """)
        escolha = input("Digite a opção escolhida: ")
        if not escolha.isnumeric():
            print("Digite apenas o número da operação escolhida.")
            escolha = 0
        else:
            escolha = int(escolha)
            if 0 > escolha > 2:
                print("Digite um valor válido para a operação.")
            elif escolha == 0:
                escolha = -1

        return escolha


def criacao_conta_bancaria(cliente_logado):
    total_contas_cliente = 0
    informacoes_conta = list()
    for index in cliente_logado:
        total_contas_cliente += 1
    total_contas_cliente -= 2
    if total_contas_cliente >= 1:
        print(f"Você tem um total de {total_contas_cliente} contas criadas")
        print("Deseja criar outra conta?")
        escolha = input("""
1 - Criar Conta
0 - Menu anterior
Digite sua opção: """)
        escolha = int(escolha)
        if escolha == 1:
            informacoes_conta = [0, 3, ""]
            print("Nova conta criada com sucesso!")
        elif escolha == 0:
            print("Cancelando operação.")
        else:
            print("Valor inválido! Cancelando operação.")

    else:
        informacoes_conta = [0, 3, ""]
        print("Nova conta criada com sucesso!")

    return informacoes_conta


