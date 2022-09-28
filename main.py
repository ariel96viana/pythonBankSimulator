from funcoes_banco import FuncoesBanco

operacao = 0
saldo_total = 0
saque_diario = 3
extrato = ""


clientes_banco = {}
contas_banco = {}

funcionamento = FuncoesBanco

print(f"""
####### Banco Ari Stonks #######
#######    OPERAÇÕES:    #######
#   1 - Criar usuário          #
#   2 - Criar conta corrente   #
#   3 - Extrato                #
#   4 - Depósito               #
#   5 - Saque                  #
#   6 - Sair                   #
################################""")

while operacao != 6:

    operacao = int(input("Digite a operação desejada: "))

    if operacao == 1:
        clientes_banco = funcionamento.criar_cliente(clientes_banco, contas_banco)

    elif operacao == 2:
        contas_banco, clientes_banco = funcionamento.cadastrar_conta(clientes_banco, contas_banco)

    elif operacao == 3:
        funcionamento.realizar_extrato(extrato, saldo_total, saque_diario)

    elif operacao == 4:
        extrato, saldo_total = funcionamento.realizar_deposito(extrato, saldo_total)

    elif operacao == 5 and saque_diario > 0:
        extrato, saldo_total, saque_diario = funcionamento.realizar_saque(extrato, saldo_total, saque_diario)

    elif operacao == 5 and saque_diario <= 0:
        print("Saques diários excedidos!")

    elif operacao == 6:
        print("Fim da operação! Volte sempre!")
        break

    else:
        print("Operação inválida!")
