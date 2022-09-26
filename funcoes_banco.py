class FuncoesBanco:

    def __init__(self, extrato, saldo_total, saldo_diario, ):
        self.extrato = extrato
        self.saldo_total = saldo_total
        self.saldo_diario = saldo_diario

    def realizar_extrato(self, extrato, saldo_total, saldo_diario):
        print(f"\n**********EXTRATO**********")
        print("Não realizadas movimentações!" if not extrato else extrato)
        print(f"Saldo total: R${saldo_total:.2f}\n"
              f"Total de saques diários: {saldo_diario}\n"
              f"***************************\n")

    def realizar_deposito(self, extrato, saldo_total):
        valor_deposito = int(input("Qual o valor deseja depositar? "))

        if valor_deposito > 0:
            print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso!")
            saldo_total += valor_deposito
            extrato += f"Depósito - R${valor_deposito:.2f}\n"

        else:
            print("Depósito negativo, operação cancelada!")

        return extrato, saldo_total

    def realizar_saque(self, extrato, saldo_total, saldo_diario):
        valor_saque = int(input("Qual o valor deseja sacar?"))
        if valor_saque <= saldo_total:
            print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
            saldo_diario -= 1
            print(f"Saques diários disponíveis: {saldo_diario}")
            saldo_total -= valor_saque
            extrato += f"Saque - R${valor_saque:.2f}\n"
        else:
            print("Saldo insuficiente!")

        return extrato, saldo_total, saldo_diario