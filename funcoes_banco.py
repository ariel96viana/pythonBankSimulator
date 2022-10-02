class FuncoesBanco:

    def __init__(self, extrato, saldo_total, saque_diario, clientes, clientes_banco, contas_banco):
        self.extrato = extrato
        self.saldo_total = saldo_total
        self.saque_diario = saque_diario
        self.clientes = clientes
        self.clientes_banco = clientes_banco
        self.contas_banco = contas_banco

    def realizar_extrato(nome, cpf, extrato, saldo_total, saque_diario):
        print(f"\n**********EXTRATO**********")
        print(f"{nome} - {cpf}\n")
        print("Não realizadas movimentações!\n" if not extrato else extrato)
        print(f"Saldo total: R${saldo_total:.2f}\n"
              f"\nSaques disponíveis: {saque_diario}\n"
              f"***************************\n")

    def realizar_deposito(extrato, saldo_total):
        valor_deposito = int(input("Qual o valor deseja depositar? "))

        if valor_deposito > 0:
            print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso!")
            saldo_total += valor_deposito
            extrato += f"Depósito - R${valor_deposito:.2f}\n"
        else:
            print("Depósito negativo, operação cancelada!")

        return extrato, saldo_total

    def realizar_saque(extrato, saldo_total, saque_diario):
        valor_saque = int(input("Qual o valor deseja sacar?"))
        if valor_saque <= saldo_total:
            print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
            saque_diario -= 1
            print(f"Saques diários disponíveis: {saque_diario}")
            saldo_total -= valor_saque
            extrato += f"Saque - R${valor_saque:.2f}\n"
        else:
            print("Saldo insuficiente!")

        return extrato, saldo_total, saque_diario
