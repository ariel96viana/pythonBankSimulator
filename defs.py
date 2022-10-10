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
    if not clientes:
        print("Não há clientes cadastrados.")
    else:
        print("""*******Python Bank******
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
    limpar_tela()
    return escolha_cliente - 1


def menu_cliente_logged(cliente_logado):
    escolha = 0
    while not escolha:
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
    limpar_tela()
    return escolha


def criacao_conta_bancaria(cliente_logado, agencia, id_conta):
    total_contas_cliente = 0
    informacoes_conta = list()
    for _ in cliente_logado:
        total_contas_cliente += 1
    total_contas_cliente -= 2
    if total_contas_cliente >= 1:
        print(f"Você tem um total de {total_contas_cliente} contas criadas")
        print("Deseja criar outra conta?")
        escolha = input("""1 - Criar Conta
0 - Menu anterior
Digite sua opção: """)
        escolha = int(escolha)
        if escolha == 1:
            informacoes_conta = [agencia, id_conta, int(0), int(3), ""]
            print("Nova conta criada com sucesso!")
        elif escolha == 0:
            print("Cancelando operação.")
        else:
            print("Valor inválido! Cancelando operação.")

    else:
        informacoes_conta = [agencia, id_conta, int(0), int(3), ""]
        print("Nova conta criada com sucesso!")

    limpar_tela()
    return informacoes_conta


def escolher_conta(cliente_logado):
    total_contas_cliente = 0
    conta_escolhida = 0
    index_conta = 1
    for _ in cliente_logado:
        total_contas_cliente += 1
    total_contas_cliente -= 2
    if total_contas_cliente == 0:
        print("Primeiro crie uma conta, para poder administrá-la!")

    elif total_contas_cliente == 1:
        conta_escolhida = 2

    else:
        print("Qual conta deseja administrar?")
        for contas in cliente_logado[2:]:
            print(f"{index_conta} - Conta: {contas[1]} - Agência: {contas[0]}")
            index_conta += 1
        while not conta_escolhida:
            conta_escolhida = input("Digite sua opção: ")
            if not conta_escolhida.isnumeric():
                print("Digite um valor válido!")
                conta_escolhida = 0
            else:
                conta_escolhida = int(conta_escolhida)
                if conta_escolhida > index_conta:
                    print("Digite um valor válido!")
                    conta_escolhida = 0

            conta_escolhida += 1
    limpar_tela()
    return conta_escolhida


def movimentacao_conta(cliente_logado, conta_escolhida):
    agencia_banco = cliente_logado[conta_escolhida][0]
    id_conta = cliente_logado[conta_escolhida][1]
    saldo_cliente = cliente_logado[conta_escolhida][2]
    saques_cliente = cliente_logado[conta_escolhida][3]
    extrato_cliente = cliente_logado[conta_escolhida][4]
    escolha = ''

    print(f"""
*******Python Bank******
{cliente_logado[1][0]} - {cliente_logado[0]}
Conta: {id_conta} - Agência: {agencia_banco}
Movimentação da Conta
1 - Extrato 
2 - Depósito
3 - Saque
0 - Sair
Saques disponíveis: {saques_cliente}
************************
    """)
    while not escolha:
        escolha = input("Digite sua opção: ")

        if not escolha.isnumeric():
            print("Digite um valor válido!")
            escolha = 0
        else:
            escolha = int(escolha)
            if 0 > escolha > 3:
                print("Digite um valor válido!")
                escolha = 0

        if escolha == 1:
            limpar_tela()
            extrato(saldo_cliente, id_conta, agencia_banco,
                    saques_diarios=saques_cliente,
                    extrato_total=extrato_cliente)

        elif escolha == 2:
            limpar_tela()
            saldo_cliente, extrato_cliente = deposito(saldo_cliente, extrato_cliente)

        elif escolha == 3:
            limpar_tela()
            saques_cliente, saldo_cliente, extrato_cliente = saque(saques_diarios=saques_cliente,
                                                                   saldo=saldo_cliente,
                                                                   extrato_total=extrato_cliente)
        else:
            escolha = -1

    return escolha, saldo_cliente, saques_cliente, extrato_cliente


def extrato(saldo, id_conta, agencia_banco, *, saques_diarios, extrato_total):
    print("-------EXTRATO TOTAL-------\n")
    print(f"Conta: {id_conta} - Agência: {agencia_banco}")
    print(extrato_total) if extrato_total else print("Sem movimentações na conta")
    print(f"Saldo Total: R${saldo:.2f}")
    print(f"Saques Disponíveis: {saques_diarios}")
    print("\n---------------------------")

    return extrato_total


def deposito(saldo, extrato_total):
    valor_deposito = ''

    while not valor_deposito:
        print("Operação de Depósito. Para cancelar insira o valor 0.")
        valor_deposito = input("Digite o valor de depósito: ")

        if not valor_deposito.isnumeric():
            print("Digite um valor válido para depósito!")
            valor_deposito = ''
        else:
            valor_deposito = int(valor_deposito)

            if valor_deposito < 0:
                print("Valor para depósito inválido!")
                valor_deposito = ''

            elif valor_deposito == 0:
                print("Operação cancelada!")
                valor_deposito = 1

            else:
                print(f"Depósito de R${valor_deposito:.2f} relizado com sucesso!")
                saldo += valor_deposito
                extrato_total += f"Depósito: R${valor_deposito:.2f}\n"

    return saldo, extrato_total


def saque(*, saques_diarios, saldo, extrato_total):
    valor_saque = ''

    while not valor_saque:
        print("Operação de Saque. Para cancelar insira o valor 0.")
        valor_saque = input("Digite o valor de saque: ")
        if not valor_saque.isnumeric():
            print("Digite um valor válido para saque!")
            valor_saque = ''
        else:
            valor_saque = int(valor_saque)

            if saques_diarios <= 0:
                print("Saques diários indisponíveis!")

            else:
                if valor_saque > saldo:
                    print("Saldo indisponível.")
                    valor_saque = ''

                elif valor_saque == 0:
                    print("Operação cancelada!")
                    valor_saque = 1

                else:
                    print(f"Saque de R${valor_saque:.2f} relizado com sucesso!")
                    saques_diarios -= 1
                    saldo -= valor_saque
                    extrato_total += f"Saque: R${valor_saque:.2f}\n"

    return saques_diarios, saldo, extrato_total
