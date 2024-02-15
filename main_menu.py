from Management.desportista import *
from Repetitive_actions.support_functions import *
dados_inseridos = False
while True: 
    linha()
    print('MENU PRINCIPAL'.center(20))
    linha()
    resposta = menu(['Introduzir novo desportista','Alterar dados do desportista','Remover desportista','Registar treino','Remover treino','Gravar dados','Carregar dados','Consultas','Sair'])
    linha2()

    if resposta == 1:
        if dados_inseridos:
            print('Deve fazer o registo do desportista que foi anteriormente inserido.')
        else:
            dados = novo()
            if dados:
                print(dados)
                print('')
                print('Dados lidos com sucesso!')
                dados_inseridos = True
            else:
                print('Erro ao inserir dados do desportista.')
        
       

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

