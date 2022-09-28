class FuncoesBanco:

    def __init__(self, extrato, saldo_total, saque_diario, clientes, contas_banco):
        self.extrato = extrato
        self.saldo_total = saldo_total
        self.saque_diario = saque_diario
        self.clientes = clientes
        self.contas_banco = contas_banco

    def criar_cliente(contas_banco):
        nome_cliente = input("Digite seu nome: ").strip()
        if nome_cliente in contas_banco:
            print("Cliente já existente!")
        else:
            cpf_cliente = input("Digite o CPF: ").strip()
            contas_banco[nome_cliente] = {
                "cpf": cpf_cliente
            }
            print(f"Cliente {nome_cliente} cadastrado!")
        return contas_banco

    def realizar_extrato(extrato, saldo_total, saque_diario):
        print(f"\n**********EXTRATO**********")
        print("Não realizadas movimentações!" if not extrato else extrato)
        print(f"Saldo total: R${saldo_total:.2f}\n"
              f"Total de saques diários: {saque_diario}\n"
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
