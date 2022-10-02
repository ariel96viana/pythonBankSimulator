class FuncoesBancoTest:

    def __init__(self, clientes_banco, contas_banco):
        self.clientes_banco = clientes_banco
        self.contas_banco = contas_banco

    def cadastrar_cliente_banco(clientes_banco, contas_banco):
        cliente_selecao = list()
        nome_cliente = input("Digite seu nome: ").strip()
        cpf_cliente = input("Digite seu cpf: ").strip()
        validacao = 1

        if clientes_banco:
            for cpf in clientes_banco:
                if cpf[1] == cpf_cliente:
                    validacao = 0
                else:
                    for cpf_banco in contas_banco:
                        if cpf_banco[1] == cpf_cliente:
                            validacao = 0
        if validacao == 1:
            cliente_selecao.append(nome_cliente)
            cliente_selecao.append(cpf_cliente)
            print(f"Cliente {nome_cliente} cadastrado!")
        else:
            print("Cliente já cadastrado")

        return cliente_selecao
