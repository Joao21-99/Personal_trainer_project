from Desportista import *
from repetitive_actions import *
while True: 
    linha()
    print('MENU PRINCIPAL'.center(20))
    linha()
    resposta = menu(['Introduzir novo desportista','Alterar dados do desportista','Remover desportista','Registar treino','Remover treino','Gravar dados','Carregar dados','Consultas','Sair'])
    linha2()

    if resposta == 1:
        dados = novo()
        print(dados)
        print('')
        print('Dados lidos com sucesso!')

    elif resposta == 2:
       modificar(dados)
    
    elif resposta == 3:
        remover(dados)

    elif resposta == 9:
        break

    else:
        print()
        print('Opção inválida. Tente de novo')
        print()

