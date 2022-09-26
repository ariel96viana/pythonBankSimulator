from funcoes_banco import FuncoesBanco

operacao = 0
saldo_total = 0
saldo_diario = 3
extrato = ""
funcionamento = FuncoesBanco

print(f"""
####### Banco Ari Stonks #######
#######    OPERAÇÕES:    #######
#   1 - Extrato                #
#   2 - Depósito               #
#   3 - Saque                  #
#   4 - Sair                   #
################################""")

while operacao != 4:
    operacao = int(input("Digite a operação desejada: "))

    if operacao == 1:

        funcionamento.realizar_extrato(extrato, saldo_total, saldo_diario)

    elif operacao == 2:

        extrato, saldo_total = funcionamento.realizar_deposito(extrato, saldo_total)

    elif operacao == 3 and saldo_diario > 0:

        extrato, saldo_total, saldo_diario = funcionamento.realizar_saque(extrato, saldo_total, saldo_diario)

    elif operacao == 3 and saldo_diario <= 0:
        print("Saques diários excedidos!")

    elif operacao == 4:
        print("Fim da operação! Volte sempre!")
        break

    else:
        print("Operação inválida!")
