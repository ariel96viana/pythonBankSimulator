class FuncoesClientes:

    def __init__(self, cadastrar_conta, contas_banco, conta_selecionada):
        self.cadastrar_conta = cadastrar_conta
        self.contas_banco = contas_banco
        self.conta_selecionada = conta_selecionada

    def criar_cliente(self, contas_banco):
        nome_cliente = input("Digite seu nome: ").strip()
        if nome_cliente in self or nome_cliente in contas_banco:
            print("Cliente já existente!")
        else:
            self[nome_cliente] = {
                "nome": nome_cliente
            }
            print(f"Cliente {nome_cliente} cadastrado!")

        return self

    def cadastrar_conta(self, contas_banco):
        print("Qual cliente deseja vincular a conta?")

        for cliente in self:
            print(f"{cliente}")

        contas_adicionar = input("Digite a sua opção: ").strip()
        if contas_adicionar not in self:
            print("Cliente não encontrado, para criar uma conta, primeiro cadastre-se.")

        else:
            contas_banco[contas_adicionar] = self[contas_adicionar]
            del self[contas_adicionar]
            contas_banco[contas_adicionar] = {
                "Saldo": 0,
                "Saques Diários": 3,
                "Extrato": ""
            }
            print(f"Seja bem-vindo(a) {contas_adicionar}!\nConta criada com sucesso!")

        return contas_banco, self

    def escolher_conta(self, conta_selecionada):
        print("Qual conta deseja acessar?")

        for cliente in self:
            print(f"{cliente}")

        conta_escolher = input("Digite a sua opção: ").strip()
        if conta_escolher not in self:
            print("Cliente não encontrado, para criar uma conta, primeiro cadastre-se.")

        else:
            conta_selecionada[conta_escolher] = self[conta_escolher]

        return conta_selecionada
