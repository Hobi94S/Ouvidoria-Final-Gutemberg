from operacoesbd import *
from OuvidoriaFinalBack import *

conn = criarConexao('localhost','root','12345678aA!','Ouvidoria')

print('Bem-vindo ao Sistema de Ouvidoria de Miguel e Gutemberg')

while True:
    print('MENU')
    print(
        '1) Listar Manifestações \n2) Adicionar uma nova Manifestação \n3) Buscar Manifestação por Cód. \n4) Remover Manifestação \n5) Número de Manifestações \n6) Sair')
    opcao = int(input('Selecione a opção: '))
    if opcao == 1:
        listarmanifestacoes(conn)

    elif opcao == 2:
        addmanifestacoes(conn)

    elif opcao == 3:
        buscarmanifestacoes(conn)

    elif opcao == 4:
        removermanifestacao(conn)

    elif opcao == 5:
        totalizarmanifestacao(conn)

    elif opcao != 6:
        print('\n!Erro! Valor inválido\n')

    else:
        break
print('\n Obrigado por usar a Ouvidoria!')

endconn = encerrarConexao(conn)




