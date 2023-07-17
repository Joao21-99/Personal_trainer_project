from repetitive_actions import errorNumeric, errorString, errorDate
# Funções base
def novo():
    lista_clientes = []
    while True:
        nome = input('Nome: ').strip()
        errorString(nome)
        num_tel = input('Nº telemovel: ')
        errorNumeric(lengthNumberPhone(num_tel))
        morada = input('Morada: ').strip()
        cc = input('Cartão de cidadão: ')
        data_nasc = errorDate()
        nivel = input('Nível: ')
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

#Funções de suporte
def lengthNumberPhone(num):
    while True:
        if len(num) == 9:
            break
        else:
            print('Um número de telefone deve ter 9 algarismos.')
            num = input('Tente de novo.')
    return num

