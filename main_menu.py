from Management.Desportista import *
from Management.Dados import *
from Repetitive_actions.support_functions import *

dados_inseridos = False
arq = 'dados.json'
if not arquivoExiste(arq):
    criarArquivo(arq)
        
while True: 
    linha()
    print('MENU PRINCIPAL'.center(20))
    linha()
    resposta = menu(['Introduzir novo desportista','Alterar dados do desportista','Remover desportista', 'Gravar dados','Registar treino','Remover treino','Carregar dados','Consultas','Sair'])
    linha2()

    if resposta == 1:
        if dados_inseridos:
            print('Deve gravar os dados do(s) desportista(s) inserido(s) anteriormente.')
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
           dados_inseridos = remover(dados,dados_inseridos)
      except(NameError):
            print('ERRO! Nenhum desportista foi inserido.')

    elif resposta == 4:
        dados_inseridos = False
        try:
            adicionarDesportistas(arq, dados)
        except(NameError):
            print('ERRO! Nenhum desportista foi inserido.')

    elif resposta == 9:
        break

    else:
        print()
        print('Opção inválida. Tente de novo')
        print()