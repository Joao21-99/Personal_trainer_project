from repetitive_actions import errorNumeric, errorString, errorDate, validateNumber, validateLevel
def novo():
    lista_clientes = []
    while True:
        nome = errorString(input('Nome: ').strip())
        num_tel=validateNumber(input('Nº telemovel: '),l=9)
        morada = input('Morada: ').strip()
        cc = validateNumber(input('Cartão de cidadão: '),l=8)
        data_nasc = errorDate()
        nivel = validateLevel(input('Niveis: Básico\nMédio\nAvançado\nPro\nNível: '))
        limit = input('Limitações: ')
        cliente = {'NOME': nome, 'TELEMÓVEL': num_tel, 'MORADA': morada, 'CARTÃO DE CIDADÃO':cc,'DATA DE NASCIMENTO': data_nasc, 'NÍVEL': nivel, 'LIMITAÇÕES': limit}
        lista_clientes.append(cliente)
        resp = str(input('Pretende continuar? (S/N)')).upper().strip()
        if resp == 'N':
            break
    return lista_clientes

def modificar(lst):
    while True:
        nome = (input('Selecione o nome do desportista: '))
        errorString(nome)
        for desp in lst:
            for k,v in desp.items():
                if nome ==v:
                        resp = input(f'Nome\n-Nº telemovel:\n-Morada\n-Cartão de cidadão\n- Data de nascimento\nNivel\nLimitações\nOlá {v}, que informação pretende alterar? ')
                        
                        if resp in desp:
                                altera = input(f'{resp}: ')
                                desp.update({resp: altera}) 
                                print(f'\nAlteração bem sucedida!\n{desp}')
                                break 
                                
                        else:
                            print('Reposta inválida')
                            break
                            
          
                     
        if nome not in desp['NOME']:
            print('Atleta não encontrado.\nCertifique-se que escreveu o nome corretamente (Nome e Apelido).')
        questao = input('Pretende continuar? [S/N]').upper().strip()
        if questao == 'N':
            break

def remover(lst):
      while True:
        nome = (input('Selecione o nome do desportista: '))
        for desp in lst:
            for k,v in desp.items():
                if nome == v:
                    lst.remove(desp)
                    print(f'\nDesportista {nome} removido com sucesso! ')
                    print(lst)
                    break
        if nome not in desp['NOME']:
            print('Atleta não encontrado.\nCertifique-se que escreveu o nome corretamente (Nome e Apelido).')
        questao = input('Pretende continuar? [S/N]').upper().strip()
        if questao == 'N':
            break




