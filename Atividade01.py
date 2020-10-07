a = 1
saldo = 2000.00
deposito = 0.0
saque = 0.0
transf = 0.0
encerrar = ""
senha = ""
confirmarSenha = ""
pessoasCadastradas = {}
conta = ""

def validaNome(nomeV):
    global nome

    if len(nomeV) < 3:
        nome = input("É preciso que seu nome tenha mais de três letras, por favor, digite seu nome novemente: ")
        validaNome(nome)

def validaSobrenome(sobrenomeV):
    global sobrenome

    if len(sobrenomeV) < 3:
        sobrenome = input("É preciso que seu sobrenome tenha mais de três letras, por favor, digite seu sobrenome novemente: ")
        validaSobrenome(sobrenome)

def validaEmail(emailV):
    global email
    separar = []

    for i in emailV:
        separar.append(i)

    if not("@" in separar[1:-1]):
        email = input("Forma de E-mail invalido, por favor, digite seu E-mail novamente: ")
        validaEmail(email)

def validaSenha(senhaV):
    global senha
    digitos = ["0","1","2","3","4","5","6","7","8","9"]
    caracteresEspeciais = []

    for i in range(32,48):
        caracteresEspeciais.append(chr(i))
    for i in range(58,65):
        caracteresEspeciais.append(chr(i))
    for i in range(91,97):
        caracteresEspeciais.append(chr(i))
    for i in range(123,127):
        caracteresEspeciais.append(chr(i))

    separar = []
    for i in senhaV:
        separar.append(i)
    print(separar)

    numeros = False
    caracter = False

    for i in separar:
        if i in digitos:
            numeros = True
        if i in caracteresEspeciais:
            caracter = True

    if len(separar) < 5 or numeros == False or caracter == False:
        senha = input("Forma de senha invalida, por favor, digite sua senha novamente: ")
        validaSenha(senha)

def validaCpf(cpfV):
    global cpf

    if cpfV in pessoasCadastradas:
        cpf = input("CPF já cadastrado, por favor, digite novamente: ") 
        validaCpf(cpf)

def menu():
    global deposito
    global saque
    global transf
    global saldo
    global encerrar
    global conta

    def validaDeposito(depositoV):
        global deposito
        global saldo
        
        if depositoV < 0:
            deposito = float(input("O valor a depositar deve ser positivo, por favor, digite novamente:(0-Sair) "))
            validaDeposito(deposito)
        elif depositoV == 0:
            menu()
        else:
            pessoasCadastradas[conta][saldo] += deposito

    def validaSaque(saqueV):
        global saque
        global saldo

        if saqueV > saldo:
            saque = float(input("O valor a sacar deve ser menor que o seu saldo, por favor, digite novamente:(0-Sair) "))
            validaSaque(saque)
        elif saqueV == 0:
            menu()
        elif saque < 0:
            saque = float(input("O valor a sacar deve ser positivo, por favor, digite novamente:(0-Sair) "))
            validaSaque(saque)
        else:
            pessoasCadastradas[conta][saldo] -= saque

    def validaTransferencia(transfV):
        global transf
        global saldo

        if transfV > saldo:
            transf = float(input("O valor a transferir deve ser menor que o seu saldo, por favor, digite novamente:(0-Sair) "))
            validaTransferencia(transf)
        elif transfV == 0:
            menu()
        elif transfV < 0:
            transf = float(input("O valor a transferir deve ser positivo, por favor, digite novamente:(0-Sair) "))
            validaTransferencia(transf)
        else:
            pessoasCadastradas[conta][saldo] -= transf

    def confirmaSenha(confirmarSenha):
        if confirmarSenha == pessoasCadastradas[conta][senha]:
            pessoasCadastradas.pop(conta)
            print("Conta encerrada")
        elif confirmarSenha == "0":
            menu()
        else:
            confirmar = input("Senha errada, por favor, digite novamente:(0-Sair) ")
            confirmaSenha(confirmar)

    def validaEncerramento(encerrarV):
        global encerrar

        if encerrarV == "1":
            confirmar = input("Digite sua senha para confirmar:(0-Sair) ")
            confirmaSenha(confirmar)
        elif encerrarV == "0":
            menu()
        else:
            encerrar = input("Opção inválida, digite outra:(0-Sair/1-Confirmar) ")
            validaEncerramento(encerrar)

    def iniciaConta(contaV):
        global conta

        conta = input("Para acessar sua conta, digite seu cpf: ")
        login = input("Digite sua senha: ")
        if conta in pessoasCadastradas:
            if login == pessoasCadastradas[conta]["Senha"]:
                print("Login feito com sucesso!")
            else:
                print("Senha incorreta")
                iniciaConta(conta)
        else:
            print("CPF digitado não está registrado no nosso banco, por favor, tente novemente")
            iniciaConta(conta)

    iniciaConta(conta)

    opcao = int(input("0-Sair\n1-Depositar\n2-Sacar\n3-Conferir Saldo\n4-Transferir\n5-Encerrar Conta\nO que você deseja fazer? "))

    if opcao == 1:
        deposito = float(input("Quanto irá depositar?(0-sair) "))
        validaDeposito(deposito)
        menu()
    elif opcao == 2:
        saque = float(input("Quanto irá sacar?(0-sair) "))
        validaSaque(saque)
        menu()
    elif opcao == 3:
        print("Seu saldo é de: R$", saldo)
        menu()
    elif opcao == 4:
        transf = float(input("Quanto irá transferir?(0-sair) "))
        validaTransferencia(transf)
        menu()
    elif opcao == 5:
        encerrar = input("Você quer mesmo encerrar sua conta?(0-Sair/1-Confirmar) ")
        validaEncerramento(encerrar)
    elif opcao == 0:
        pass
    else:
        print("Opção não é válida")
        menu()

def validaCliente():
    cliente = input("Qual cliente deseja consultar?(Digite o CPF/0-Sair) ")

    if cliente in pessoasCadastradas:
        print(pessoasCadastradas[cliente])
    elif cliente == "0":
        areaAdm()
    else:
        print("CPF digitado ainda não foi cadastrado.")
        validaCliente()

def validaDeletaCliente():
    cliente = input("Qual cliente deseja deletar?(Digite o CPF/0-Sair) ")

    if cliente in pessoasCadastradas:
        print(pessoasCadastradas[cliente])
        confirmaDelete = ("Tem certeza que deseja deletar esse cliente?(0-Não/1-Sim) ")
        if confirmaDelete == "1":
            pessoasCadastradas.pop(cliente)
            print("Conta deletada")
        elif confirmaDelete == "0":
            validaDeletaCliente()
        else:
            print("Opção digitada não é válida")
            validaDeletaCliente()
    elif cliente == "0":
        areaAdm()
    else:
        print("CPF digitado ainda não foi cadastrado.")
        validaCliente()

def atualizaDados():
    cliente = input("Qual cliente terá as informasções atualizadas?(Digite o CPF/0-Sair) ")

    if cliente in pessoasCadastradas:
        print(pessoasCadastradas[cliente])
        confirmaAtualizar = ("Tem certeza que deseja atualizar esse cliente?(0-Não/1-Sim) ")
        if confirmaAtualizar == "1":
            input("0-Sair\n1-Nome\n2-Sobrenome\n3-CPF\n4-Endereço\n5-E-mail\n6-Celular\n7-Senha\nQual será a informação atualizada? ")

            if confirmaAtualizar == "1":
                nome = input("Qual é o nome atualizado? ")
                validaNome(nome)
                pessoasCadastradas[cliente]["Nome"] = nome
            elif confirmaAtualizar == "2":
                sobrenome = input("Qual é o sobrenome atualizado? ")
                validaSobrenome(sobrenome)
                pessoasCadastradas[cliente]["Sobrenome"] = sobrenome
            elif confirmaAtualizar == "3":
                cpf = input("Qual é o CPF atualizado? ")
                validaCpf(cpf)
                pessoasCadastradas[cliente]["CPF"] = cpf 
                pessoasCadastradas[cliente] = pessoasCadastradas[cpf]
                pessoasCadastradas.pop(cliente)
            elif confirmaAtualizar == "4":
                endereco = input("Qual é o endereço atualizado? ")
                pessoasCadastradas[cliente]["Endereço"] = endereco
            elif confirmaAtualizar == "5":
                email = input("Qual é o E-mail atualizado? ")
                validaEmail(email)
                pessoasCadastradas[cliente]["E-mail"] = email
            elif confirmaAtualizar == "6":
                celular = input("Qual é o celular atualizado? ")
                pessoasCadastradas[cliente]["Celular"] = celular
            elif confirmaAtualizar == "7":
                senha = input("Qual será a senha atualizada? ")
                validaSenha()
                pessoasCadastradas[cliente]["Senha"] = senha
            elif confirmaAtualizar == "0":
                atualizaDados()
            else:
                print("Opção digitada é inválida")

        elif confirmaAtualizar == "0":
            atualizaDados()
        else:
            print("Opção digitada não é válida")
            atualizaDados()
    elif cliente == "0":
        areaAdm()
    else:
        print("CPF digitado ainda não foi cadastrado.")
        validaCliente()

def areaAdm():


    adm = input("1-Consultar um cliente\n2-Consultar lista de cliente\n3-Deletar um cliente\n4-Atualizar dados de um cliente\nO que você deseja fazer? ")

    if adm == "1":
        validaCliente()
        areaAdm()
    elif adm == "2":
        print(pessoasCadastradas)
        areaAdm()
    elif adm == "3":
        validaDeletaCliente()
        areaAdm()
    elif adm == "4":
        atualizaDados()
        areaAdm()

while a > 0:

    a = int(input("0-Sair\n1-Cadastro\n2-Opções de Conta\n3-Área Administrativa\nO que você deseja fazer: "))

    if a == 1:
        nome = input("Digite o seu nome: ")
        validaNome(nome)
        sobrenome = input("Digite seu sobrenome: ")
        validaSobrenome(sobrenome)
        cpf = input("Digite o seu CPF: ")
        validaCpf(cpf)
        endereco = input("Digite o seu endereço: ")
        email = input("Digite o seu E-mail: ")
        validaEmail(email)
        celular = input("Digite o seu celular: ")
        senha = input(("Digite a sua senha:(É preciso ter pelo menos 5 dígitos e ter pelo menos 1 número e 1 caractere especial) "))
        validaSenha(senha)
        pessoasCadastradas[cpf] = {
            "Nome" : nome,
            "Sobrenome" : sobrenome,
            "CPF" : cpf,
            "Endereço" : endereco,
            "E-mail" : email,
            "Celular" : celular,
            "Senha" : senha,
            "Saldo" : saldo}

        print("Cadastro efetuado com sucesso!")

    if a == 2:
        menu()

    if a == 3:
        usuarioAdm = input("Qual é o seu usuário? ")
        senhaAdm = input("Qual é sua senha? ")

        if usuarioAdm == "admin" and senhaAdm == "admin": 
            areaAdm()
        else:
            print("Usuário ou senha incorretos")

    if a > 3:
        print("Opção inválida")
