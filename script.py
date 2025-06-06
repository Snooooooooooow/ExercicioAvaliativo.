class Cliente:
    def  __init__(self, cpf, nome, idade, rendaMensal, scoreCredito):
        self.cpf=cpf
        self.nome=nome
        self.idade=idade
        self.rendaMensal=rendaMensal
        self.scoreCredito=scoreCredito

cliente1 = Cliente(165,"Daniel Teixeira",17,1000,100)
cliente2 = Cliente(667,"Rafael Rocha", 27, 5000, 800)
cliente3 = Cliente(190,"Gabriel Silva", 19, 2000, 600)

while True:
    cpf = input("informe o cpf: ")
    if (cpf == "165" ):
        print(
         "\nCpf:           ", cliente1.cpf,
         "\nNome:          ", cliente1.nome,
         "\nIdade:         ", cliente1.idade,
         "\nRenda mensal:  ", cliente1.rendaMensal,
         "\nScore credito: ", cliente1.scoreCredito
    )
        if (cliente1.rendaMensal < 2000) and (cliente1.scoreCredito < 600):
            print("\nCredito não aprovado por renda e score")
        elif cliente1.rendaMensal < 2000 :
            print("\nCredito não aprovado por renda")
        elif cliente1.scoreCredito < 600 :
            print("\nCredito não aprovado por score")
        else:
            print("\nCredito aprovado")
        break

    elif (cpf == "667" ):
        print(
            "\nCpf:           ", cliente2.cpf,
            "\nNome:          ", cliente2.nome,
            "\nIdade:         ", cliente2.idade,
            "\nRenda mensal:  ", cliente2.rendaMensal,
            "\nScore credito: ", cliente2.scoreCredito,
    )
        if (cliente2.rendaMensal < 2000) and (cliente2.scoreCredito < 600):
            print("\nCredito não aprovado por renda e score")
        elif cliente2.rendaMensal < 2000 :
            print("\nCredito não aprovado por renda")
        elif cliente2.scoreCredito < 600 :
            print("\nCredito não aprovado por score")
        else:
            print("\nCredito aprovado")
        break

    elif (cpf == "190" ):
        print(
            "\nCpf:           ", cliente3.cpf,
            "\nNome:          ", cliente3.nome,
            "\nIdade:         ", cliente3.idade,
            "\nRenda mensal:  ", cliente3.rendaMensal,
            "\nScore credito: ", cliente3.scoreCredito,
    )
        if (cliente3.rendaMensal < 2000) and (cliente3.scoreCredito < 600):
            print("\nCredito não aprovado por renda e score")
        elif cliente3.rendaMensal < 2000 :
            print("\nCredito não aprovado por renda")
        elif cliente3.scoreCredito < 600 :
            print("\nCredito não aprovado por score")
        else:
            print("\nCredito aprovado")
        break
    else:
        print("⚠️⚠️⚠️O usuario não foi encontrado, tente novamente...")