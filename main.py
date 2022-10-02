from funcoes_banco import FuncoesBanco
from funcoes_banco_teste import FuncoesBancoTest
from funcoes_clientes import FuncoesClientes

operacao = 0

clientes_banco = list()
contas_banco = list()
id_cliente = int

funcionamento = FuncoesBanco
funcionamento_test = FuncoesBancoTest
selecao = FuncoesClientes

print(f"""
####### Banco Ari Stonks #######
#######    OPERAÇÕES:    #######
#   1 - Cadastrar usuário      #
#   2 - Criar conta corrente   #
#   3 - Entrar na conta        #
#   4 - Sair                   #
################################""")

while operacao != 4:
    operacao = int(input("Digite a operação desejada: "))

    if operacao == 1:
        clientes_banco.append(selecao.cadastrar_cliente(clientes_banco, contas_banco))
        if not clientes_banco[-1]:
            clientes_banco.pop()

    elif operacao == 2:
        contas_banco.append(selecao.criar_conta(clientes_banco))
        if not contas_banco[-1]:
            contas_banco.pop()

    elif operacao == 3:
        id_cliente, operacao = selecao.escolher_conta(contas_banco)
        if id_cliente:
            break

print(f"""
####### Banco Ari Stonks #######
#######    OPERAÇÕES:    #######
  Bem vindo(a) {contas_banco[id_cliente][0]}
#   1 - Extrato                #
#   2 - Depósito               #
#   3 - Saque                  #
#   4 - Menu anterior          #
#   5 - Sair                   #
################################""")

# saldo_total = contas_banco[id_cliente][4]
# saque_diario = contas_banco[id_cliente][5]
# extrato = contas_banco[id_cliente][6]

while operacao != 6:

    operacao = int(input("Digite a operação desejada: "))

    if operacao == 1:
        funcionamento.realizar_extrato(contas_banco[id_cliente][0],
                                       contas_banco[id_cliente][1],
                                       contas_banco[id_cliente][6],
                                       saldo_total=contas_banco[id_cliente][4],
                                       saque_diario=contas_banco[id_cliente][5])

    elif operacao == 2:
        contas_banco[id_cliente][6], contas_banco[id_cliente][4] = funcionamento.realizar_deposito(
                                                                        contas_banco[id_cliente][6],
                                                                        contas_banco[id_cliente][4])

    elif operacao == 3 and contas_banco[id_cliente][5] > 0:
        contas_banco[id_cliente][6], contas_banco[id_cliente][4], contas_banco[id_cliente][
            5] = funcionamento.realizar_saque(extrato=contas_banco[id_cliente][6],
                                              saldo_total=contas_banco[id_cliente][4],
                                              saque_diario=contas_banco[id_cliente][5])

    elif operacao == 3 and contas_banco[id_cliente][5] <= 0:
        print("Saques diários excedidos!")

    elif operacao == 5:
        print("Fim da operação! Volte sempre!")
        break

    else:
        print("Operação inválida!")
