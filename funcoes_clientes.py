class FuncoesClientes:

    def __init__(self, cadastrar_conta, contas_banco, conta_selecionada):
        self.cadastrar_conta = cadastrar_conta
        self.contas_banco = contas_banco
        self.conta_selecionada = conta_selecionada

    def cadastrar_cliente(self, contas_banco):
        cliente_selecao = list()
        nome_cliente = input("Digite seu nome: ").strip()
        cpf_cliente = input("Digite seu cpf: ").strip()
        validacao = 1

        if self:
            for cpf in self:
                if cpf[1] == cpf_cliente:
                    validacao = 0

        if contas_banco:
            for cpf in contas_banco:
                if cpf[1] == cpf_cliente:
                    validacao = 0

        if validacao == 1:
            cliente_selecao.append(nome_cliente)
            cliente_selecao.append(cpf_cliente)
            cliente_selecao.append(input("Data de nascimento(dd/mm/aaaa):"))
            cliente_selecao.append(input(str("Endereço (rua, nº - bairro - cidade/UF): ")))

            print(f"Cliente {nome_cliente} cadastrado!")

        else:
            print("CPF já cadastrado")

        return cliente_selecao

    def criar_conta(self):
        criar_conta = list()
        print("Qual cliente deseja vincular a conta?")
        saldo = 0
        saque_diario = 3
        extrato = ""
        x = 0

        for cliente in self:
            x += 1
            print(x, "-", cliente[0])
        if not self:
            print("Não há clientes cadastrados.")
        else:
            contas_adicionar = int(input("Digite o número de sua opção: "))
            contas_adicionar -= 1

            if contas_adicionar >= x or contas_adicionar < 0:
                print("Digite uma opção válida. Ou se preferir, cadastre uma nova conta.")

            else:
                criar_conta.append(self[contas_adicionar][0])
                criar_conta.append(self[contas_adicionar][1])
                criar_conta.append(self[contas_adicionar][2])
                criar_conta.append(self[contas_adicionar][3])
                criar_conta.append(saldo)
                criar_conta.append(saque_diario)
                criar_conta.append(extrato)
                print(f"Seja bem-vindo(a) {self[contas_adicionar][0]}!\nConta criada com sucesso!")
                self.pop(contas_adicionar)
        return criar_conta

    def escolher_conta(self):

        x = 0

        for cliente in self:
            x += 1
            print(x, "-", cliente[0])
        if not self:
            print("Não há clientes com contas cadastradas.")

        else:
            conta_escolher = int(input("Digite o numero da sua opção: "))
            conta_escolher -= 1

        if conta_escolher < 0 or conta_escolher >= x:
            print("Cliente não encontrado, se desejar, crie uma conta ou cadastre-se!")

        else:
            operacao = 4

        return conta_escolher, operacao
