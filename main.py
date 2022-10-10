import defs
from time import sleep

clientes = list()

nome = ''
cpf = ''
data_nascimento = ''
endereco = ''
AGENCIA = "0001"
id_conta = 1

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

            while escolha != -1:
                escolha = defs.menu_cliente_logged(cliente_logado)

                if escolha == 1:
                    cliente_logado.append(defs.criacao_conta_bancaria(cliente_logado,
                                                                      agencia=AGENCIA,
                                                                      id_conta=id_conta))

                    if not cliente_logado[-1]:
                        cliente_logado.pop()
                    else:
                        id_conta += 1

                elif escolha == 2:
                    conta_escolhida = defs.escolher_conta(cliente_logado)

                    if conta_escolhida > 1:
                        while escolha != -1:
                            movimentacoes = cliente_logado[conta_escolhida]
                            escolha, movimentacoes[2], movimentacoes[3], movimentacoes[4] = defs.movimentacao_conta(
                                                                                                        cliente_logado,
                                                                                                        conta_escolhida)
                            cliente_logado[conta_escolhida] = movimentacoes

    elif escolha == 0:
        print("Agradecemos sua preferência, volte sempre!")
        sleep(2)
        break
