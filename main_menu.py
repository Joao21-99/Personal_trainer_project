from Desportista import *
from repetitive_actions.support_functions import *
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
        try:
            modificar(dados)
        except(NameError):
            print('ERRO! Nenhum desportista foi inserido.')
    
    elif resposta == 3:
      try:
            remover(dados)
      except(NameError):
            print('eERRO! Nenhum desportista foi inserido.')

    elif resposta == 9:
        break

    else:
        print()
        print('Opção inválida. Tente de novo')
        print()

