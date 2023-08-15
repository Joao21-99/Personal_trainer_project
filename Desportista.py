from repetitive_actions import *
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
    while True:
        id = readInt('Selecione o seu ID: ')
        for desp in lst:
            for k,v in desp.items():
                if id == v:
                        resp = input(f'Nome\n-Nº telemovel:\n-Morada\n-Cartão de cidadão\n- Data de nascimento\nNivel\nLimitações\nOlá {desp["NOME"]}, que informação pretende alterar? ').upper()
                        
                        if resp in desp:
                                if desp[resp] == desp['NOME']:
                                    altera = errorString(input(f'{resp}: '))
                                    desp.update({resp: altera}) 
                                    print(f'\nAlteração bem sucedida!\n{desp}')

                                elif desp[resp] == desp['TELEMOVEL']:
                                    altera = validateNumber(input(f'{resp}: '), l=9)
                                    desp.update({resp: altera}) 
                                    print(f'\nAlteração bem sucedida!\n{desp}')
                                    
                                elif desp[resp] == desp['MORADA']:
                                    altera = input(f'{resp}: ')
                                    desp.update({resp: altera}) 
                                    print(f'\nAlteração bem sucedida!\n{desp}')

                                elif desp[resp] == desp['CARTÃO DE CIDADÃO']:
                                    altera = validateNumber(input(f'{resp}: '),l=8)
                                    desp.update({resp: altera}) 
                                    print(f'\nAlteração bem sucedida!\n{desp}')

                                elif desp[resp] == desp['DATA DE NASCIMENTO']:
                                    altera = errorDate()
                                    desp.update({resp: altera}) 
                                    print(f'\nAlteração bem sucedida!\n{desp}')    
                                elif desp[resp] == desp['NIVEL']:
                                    altera = input(f'{resp}: ')
                                    desp.update({resp: altera}) 
                                    print(f'\nAlteração bem sucedida!\n{desp}') 

                                elif desp[resp] == desp['LIMITAÇÕES']:
                                    altera = input(f'{resp}: ')
                                    desp.update({resp: altera}) 
                                    print(f'\nAlteração bem sucedida!\n{desp}')  
                               
                        else:
                            print('Reposta inválida')
                            break
                            
          
                     
        if id != desp['ID']:
            print('Atleta não encontrado.')
        questao = input('Pretende continuar? [S/N]').upper().strip()
        if questao == 'N':
            break

def remover(lst):
      while True:
        id =  readInt('Selecione o seu ID: ')
        for desp in lst:
            for k,v in desp.items():
                if id == v:
                    lst.remove(desp)
                    print(f'\nDesportista {desp["NOME"]} removido com sucesso! ')
                    print(lst)
                    break
        if id not in desp['ID']:
            print('Atleta não encontrado.')
        questao = input('Pretende continuar? [S/N]').upper().strip()
        if questao == 'N':
            break




