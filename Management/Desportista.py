
from Repetitive_actions.support_functions import *
def novo(nivel = 'BASICO', limit = 'Nenhuma'):
    lista_clientes = []
    id = 0
    while True:
        nome = errorString(input('Nome: ').strip())
        num_tel=validateNumber(input('Nº telemovel: '),l=9)
        morada = input('Morada: ').strip()
        cc = validateNumber(input('Cartão de cidadão: '),l=8)
        data_nasc = errorDate()
        nivel = validateLevel()
        limit = input('Limitações: ')
        id += 1
        cliente = {'ID': id, 'NOME': nome, 'TELEMOVEL': num_tel, 'MORADA': morada, 'CARTÃO DE CIDADÃO':cc,'DATA DE NASCIMENTO': data_nasc, 'NIVEL': nivel, 'LIMITAÇÕES': limit}
        lista_clientes.append(cliente)
        resp = str(input('Pretende continuar? (S/N)')).upper().strip()
        if resp == 'N':
            break
    return lista_clientes

def modificar(lst):
    try:   
        while True:
            id = readInt('Selecione o seu ID: ')
            for desp in lst:
                for k,v in desp.items():
                    if id == v:
                        while True:
                            print(f'Olá {desp["NOME"]}, que informação gostarias de alterar?')
                            resp = menu(['Nome','Nº telemóvel','Morada', 'Cartão de cidadão', 'Data de nascimento','Nível','Limitações','Voltar'])
                            if resp == 1:
                                altera = errorString(input('Nome: ').strip())
                                desp['NOME'] = altera
                                print(f'\nAlteração bem sucedida!\n{desp}')

                            elif resp == 2:
                                altera = validateNumber(input('Nº telemóvel: '), l=9)
                                desp['TELEMOVEL'] = altera
                                print(f'\nAlteração bem sucedida!\n{desp}')

                            elif resp == 3:
                                altera = input('Morada: ')
                                desp['MORADA'] = altera
                                print(f'\nAlteração bem sucedida!\n{desp}')

                            elif resp == 4:
                                altera = validateNumber(input('Cartão de cidadão: '),l=8)

                            elif resp == 5:
                                altera = errorDate()
                                desp['DATA DE NASCIMENTO'] = altera
                                print(f'\nAlteração bem sucedida!\n{desp}')

                            elif resp == 6:
                                altera = validateLevel()
                                desp['NIVEL'] = altera
                                print(f'\nAlteração bem sucedida!\n{desp}')

                            elif resp == 7:
                                altera = input('Limitações: ')
                                desp['LIMITAÇÕES'] = altera
                                print(f'\nAlteração bem sucedida!\n{desp}')
                            elif resp ==8:
                                break
                            else:
                                print('Opção inválida')
                            questao = input('Pretende continuar? [S/N]').upper().strip()
                            linha2()
                            if questao == 'N':
                                break

                            
                            
            if id != desp['ID']:
                print('Atleta não encontrado.')
            questao = input('Pretende continuar? [S/N]').upper().strip()
            if questao == 'N':
                break
    except (UnboundLocalError):
        print('ERRO! Nenhum desportista foi inserido.')
        print()
             


def remover(lst, dados_inseridos):
    try:  
      while True:
        id =  readInt('Selecione o seu ID: ')
        for desp in lst:
            for k,v in desp.items():
                if id == v:
                    lst.remove(desp)
                    print(f'\nDesportista {desp["NOME"]} removido com sucesso! ')
                    print(lst)
                    break
        if lst == []:
            print('Não existe mais nenhum desportista inserido.')
            dados_inseridos = False
            break

        if id != desp['ID']:
            print('Atleta não encontrado.')
        questao = input('Pretende continuar? [S/N]').upper().strip()

        if questao == 'N':
            break
    except(UnboundLocalError):
        print('ERRO! Nenhum desportista foi inserido.') 

    return dados_inseridos     
  
