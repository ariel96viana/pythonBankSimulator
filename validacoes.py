
def valida_nome(nome):

    while not nome:
        nome = str(input("Digite o seu nome: ")).strip()
        while nome == '':
            print("Digite uma opção válida!")
            nome = str(input("Digite o seu nome: ")).strip()

        if nome:
            for letras in nome:
                if letras.isnumeric():
                    print("Não pode haver números no nome.")
                    nome = ''
                    break
    return nome.title()


def valida_cpf(cpf):

    while not cpf:
        cpf = str(input("Digite seu CPF(apenas números): "))

        while len(cpf) != 11:
            print("Digite um CPF válido, com 11 números!")
            cpf = str(input("Digite seu CPF(apenas números): "))

        if not cpf.isnumeric():
            print("O CPF não pode conter letras! Digite apenas números!")
            cpf = ''

    return cpf


def valida_nascimento(data_nascimento):

    while not data_nascimento:
        data_nascimento = str(input("Digite sua data de nascimento(apenas números): "))
        data = ''
        x = 0
        if not data_nascimento.isnumeric():
            print("A data deve conter apenas números.")
            data_nascimento = ''
        else:
            if len(data_nascimento) != 6 and len(data_nascimento) != 8:
                print("Valores digitados inválidos.")
                data_nascimento = ''
            else:
                for numero in data_nascimento:
                    x += 1
                    if x == 2 or x == 4:
                        numero += '/'
                    data += numero

                data_nascimento = data

    return data_nascimento


def valida_endereco(endereco):
    nome_rua = ""
    numero_rua = ""
    nome_bairro = ""
    nome_cidade = ""
    sigla_estado = ""

    while not endereco:
        print("Digite seu esdereço completo.")
        while not nome_rua:
            nome_rua = str(input("Nome da rua:")).title()
        while not numero_rua:
            numero_rua = str(input("Número da casa, prédio e/ou apartamento: ")).title()
        while not nome_bairro:
            nome_bairro = str(input("Nome do bairro: ")).title()
        while not nome_cidade:
            nome_cidade = str(input("Nome da cidade: ")).title()
        while not sigla_estado:
            sigla_estado = str(input("Sigla do estado(UF): ")).upper()
            if len(sigla_estado) != 2:
                print("Digite apenas a sigla do estado(UF).")
                sigla_estado = ""
        endereco = f"Endereço: {nome_rua}, {numero_rua} - {nome_bairro} - {nome_cidade}/{sigla_estado}."

    return endereco


def cliente_unico(cpf, clientes):
    if clientes:
        for user in clientes:
            if cpf == user[0]:
                print("Cliente já cadastrado!")
                return False
            else:
                return True
    else:
        return True
