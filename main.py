operacao = 0
saldoTotal = 0
valorDeposito = 0
saqueDiario = 3
extrato = ""


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
        print(f"\n**********EXTRATO**********")
        print("Não realizadas movimentações!" if not extrato else extrato)
        print(f"Saldo total: R${saldoTotal:.2f}\n"
              f"Total de saques diários: {saqueDiario}\n"
              f"***************************\n")

    elif operacao == 2:
        valorDeposito = int(input("Qual o valor deseja depositar? "))

        if valorDeposito > 0:
            print(f"Depósito de R${valorDeposito:.2f} realizado com sucesso!")
            saldoTotal += valorDeposito
            extrato += f"Depósito - R${valorDeposito:.2f}\n"

        else:
            print("Depósito negativo, operação cancelada!")

    elif operacao == 3 and saqueDiario > 0:
        valorSaque = int(input("Qual o valor deseja sacar?"))
        if valorSaque <= saldoTotal:
            print(f"Saque de R${valorSaque:.2f} realizado com sucesso!")
            saqueDiario -= 1
            print(f"Saques diários disponíveis: {saqueDiario}")
            saldoTotal -= valorSaque
            extrato += f"Saque - R${valorSaque:.2f}\n"
        else:
            print("Saldo insuficiente!")

    elif operacao == 3 and saqueDiario <= 0:
        print("Saques diários excedidos!")

    elif operacao == 4:
        print("Fim da operação! Volte sempre!")
        break

    else:
        print("Operação inválida!")
