import defs

clientes = list()

nome = ''
cpf = ''
data_nascimento = ''
endereco = ''

while True:
    escolha = defs.menu()

    if escolha == 1:        # CADASTRAR CLIENTE
        clientes.append(defs.cadastro_usuario(nome, cpf, data_nascimento, endereco, clientes))
        if not clientes[-1]:
            clientes.pop()

    elif escolha == 2:      # LOGAR EM CONTA CADASTRADA / ADMINISTRAR CONTA
        cliente_logado = defs.login_cliente(clientes)

        if cliente_logado != -1:
            cliente_logado = clientes[cliente_logado]

            escolha = defs.menu_cliente_logged(cliente_logado)

            if escolha == 1:
                cliente_logado.append(defs.criacao_conta_bancaria(cliente_logado))
                if not cliente_logado[-1]:
                    cliente_logado.pop()
        print(cliente_logado)
                # elif escolha == 2
