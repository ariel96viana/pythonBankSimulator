import defs

clientes = list()
cliente_escolhido = list()

nome = ''
cpf = ''
data_nascimento = ''
endereco = ''

while True:
    escolha = defs.menu()

    if escolha == 1:
        clientes.append(defs.cadastro_usuario(nome, cpf, data_nascimento, endereco, clientes))

    elif escolha == 2:
        cliente = defs.clientes_banco(clientes)
        cliente_escolhido = clientes[cliente]
        print(cliente_escolhido)
