from funcoes_banco import FuncoesBanco
from funcoes_clientes import FuncoesClientes

operacao = 0


clientes_banco = {}
contas_banco = {}
conta_selecionada = {}

funcionamento = FuncoesBanco
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
        clientes_banco = selecao.criar_cliente(clientes_banco, contas_banco)

    elif operacao == 2:
        contas_banco, clientes_banco = selecao.cadastrar_conta(clientes_banco, contas_banco)

    elif operacao == 3:
        conta_selecionada = selecao.escolher_conta(contas_banco, conta_selecionada)
        if conta_selecionada:
            break

nome = ""
for name in conta_selecionada:
    nome = name

print(f"""
####### Banco Ari Stonks #######
#######    OPERAÇÕES:    #######
  Bem vindo(a) {nome}
#   1 - Extrato                #
#   2 - Depósito               #
#   3 - Saque                  #
#   4 - Menu anterior          #
#   5 - Sair                   #
################################""")

saldo_total = conta_selecionada[nome]["Saldo"]
saque_diario = conta_selecionada[nome]["Saques Diários"]
extrato = conta_selecionada[nome]["Extrato"]


while operacao != 6:

    operacao = int(input("Digite a operação desejada: "))

    if operacao == 1:
        funcionamento.realizar_extrato(extrato, saldo_total, saque_diario)

    elif operacao == 2:
        extrato, saldo_total = funcionamento.realizar_deposito(extrato, saldo_total)

    elif operacao == 3 and saque_diario > 0:
        extrato, saldo_total, saque_diario = funcionamento.realizar_saque(extrato, saldo_total, saque_diario)

    elif operacao == 3 and saque_diario <= 0:
        print("Saques diários excedidos!")

    elif operacao == 5:
        print("Fim da operação! Volte sempre!")
        break

    else:
        print("Operação inválida!")
