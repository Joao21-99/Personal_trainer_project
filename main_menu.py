from Desportista import novo, modificar, remover

while True:
    print('*'*20)
    print('Menu principal')
    print('*'*20)
    print('Desportista:\n1 – Introduzir novo\n2 – Alterar dados pessoais\n3 – Remover\n')
    print('Presenças em Treino:\n4 – Registar Treino e Presenças\n5 – Remover Treino\n')
    print('Gravação:\n6 – Gravar dados\n7 - Carregar dados\n')
    print('8 - Consultas\n')
    print('0 – Sair')
    print()
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        dados = novo()
        print(dados)
        print('')
        print('Dados lidos com sucesso!')

    elif opcao == 2:
       modificar(dados)
    
    elif opcao == 3:
        remover(dados)

    else:
        break
    print()





