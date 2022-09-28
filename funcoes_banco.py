class FuncoesBanco:

    def __init__(self, extrato, saldo_total, saque_diario, clientes, clientes_banco, contas_banco):
        self.extrato = extrato
        self.saldo_total = saldo_total
        self.saque_diario = saque_diario
        self.clientes = clientes
        self.clientes_banco = clientes_banco
        self.contas_banco = contas_banco

    def criar_cliente(clientes_banco, contas_banco):
        nome_cliente = input("Digite seu nome: ").strip()
        if nome_cliente in clientes_banco or nome_cliente in contas_banco:
            print("Cliente já existente!")
        else:
            clientes_banco[nome_cliente] = {
                "nome": nome_cliente
            }
            print(f"Cliente {nome_cliente} cadastrado!")

        return clientes_banco

    def cadastrar_conta(clientes_banco, contas_banco):
        print("Qual cliente deseja vincular a conta?")

        for cliente in clientes_banco:
            print(f"{cliente}")

        contas_adicionar = input("Digite a sua opção: ").strip()
        if contas_adicionar not in clientes_banco:
            print("Cliente não encontrado, para criar uma conta, primeiro cadastre-se.")

        else:
            contas_banco[contas_adicionar] = clientes_banco[contas_adicionar]
            del clientes_banco[contas_adicionar]
            contas_banco[contas_adicionar] = {
                "Saldo": 0,
                "Saques Diários": 3
            }
        return contas_banco, clientes_banco

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
