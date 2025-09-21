from operacoesbd import *

def listarmanifestacoes(conn):
    consulta = "select * from Ouvidoriav2"
    manifestacao = listarBancoDados(conn, consulta)

    if len(manifestacao) == 0:
        print("Não existem manifestações cadastradas")
    else:
        for item in manifestacao:
            print(f'Manifestação de Código {item[0]})\nTítulo: {item[1]}\nTipo: {item[4]}\n')

def addmanifestacoes(conn):
    addtitle = input("Digite o título da sua manifestação: ")
    addautor = input("Digite o nome do Autor da manifestação: ")
    addrespond = input("Digite o nome do respondente da manifestação: ")
    while True:
        print("Selecione o tipo da manifestação:")
        print("1) Reclamação")
        print("2) Elogio")
        print("3) Sugestão")

        escolha_tipo = int(input("Digite o número da opção desejada: "))

        if escolha_tipo == 1:
            addtipo = 'Reclamação'
            break
        elif escolha_tipo == 2:
            addtipo = 'Elogio'
            break
        elif escolha_tipo == 3:
            addtipo = 'Sugestão'
            break
        else:
            print("Erro: Opção inválida! Por favor, digite 1, 2 ou 3.")

    adddescript = input("Digite a sua manifestação: ")
    consulta = 'insert into Ouvidoriav2 (title,autor,respondente,tipo,descri) values (%s,%s,%s,%s,%s)'
    valores = [addtitle, addautor, addrespond, addtipo, adddescript]

    NovaManifestacao = insertNoBancoDados(conn, consulta, valores)
    print(f"Manifestação adicionada com sucesso! O código da manifestação é: {NovaManifestacao}")

def buscarmanifestacoes(conn):
    codigoMan = int(input("Digite o código da Manifestação: "))
    consulta = "select * from Ouvidoriav2 where Cod = %s "
    valores = [codigoMan]
    ManifestList = listarBancoDados(conn, consulta, valores)

    if len(ManifestList) == 0:
        print("Nao existe manifestação para o código informado")
    else:
        for item in ManifestList:
            print(
                f'\nA Manifestação pesquisada é: {item[0]})\nTítulo:{item[1]}\nAutor:{item[2]}\nRespondente:{item[3]}\nTipo:{item[4]}\nManifestação:{item[5]}')

def removermanifestacao(conn):
    codigoMan = int(input("Digite o código da Manifestação a ser removida: "))

    consulta = 'delete from Ouvidoriav2 where Cod  = %s'
    valores = [codigoMan]

    manRemov = excluirBancoDados(conn, consulta, valores)

    if manRemov == 1:
        print(f"Manifestação de código {codigoMan} foi removida com sucesso!")
    else:
        print(f"Erro: A Manifestação de código {codigoMan} é inexistente ou já foi removida.")

def totalizarmanifestacao(conn):
    consulta = "select count(*) from Ouvidoriav2"
    quantManifest = listarBancoDados(conn, consulta)

    print(f"Atualmente existem {quantManifest[0][0]} Manifestações")


def buscarportipo(conn):
    while True:
        print("\nSelecione o tipo da manifestação:")
        print("1) Reclamação")
        print("2) Elogio")
        print("3) Sugestão")

        escolha_tipo = int(input("Digite o número da opção desejada: "))

        if escolha_tipo == 1:
            addtipo = 'Reclamação'
            break
        elif escolha_tipo == 2:
            addtipo = 'Elogio'
            break
        elif escolha_tipo == 3:
            addtipo = 'Sugestão'
            break
        else:
            print("\n!Erro! Opção inválida. Por favor, digite 1, 2 ou 3.")

    consulta = "select * from Ouvidoriav2 where tipo = %s"
    valores = [addtipo]
    ManifestList = listarBancoDados(conn, consulta, valores)

    if len(ManifestList) == 0:
        print(f"\nNenhuma manifestação do tipo '{addtipo}' foi encontrada.")
    else:
        print(f"\nManifestações do tipo '{addtipo}' encontradas:")
        for item in ManifestList:
            print(f'Código: {item[0]}\nTítulo:{item[1]}\nAutor:{item[2]}\nRespondente:{item[3]}\nTipo:{item[4]}\nManifestação:{item[5]}\n')