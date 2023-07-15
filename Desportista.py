def novo():
    from datetime import datetime
    lista_clientes = []
    while True:
        nome = input('Nome: ').strip()
        num_tel = int(input('Nº telemovel: '))
        morada = input('Morada: ').strip()
        cc = int(input('Cartão de cidadão: '))
        while True:
            data_nasc = input("Data de nascimento (formato: dd/mm/aaaa): ")
            try:
                data = datetime.strptime(data_nasc, "%d/%m/%Y")
                break  
            except ValueError:
                print("Formato de data inválido. Tente novamente.")
        nivel = input('Nível: ')
        limit = input('Limitações: ')

        cliente = {'NOME': nome, 'TELEMÓVEL': num_tel, 'MORADA': morada, 'CARTÃO DE CIDADÃO':cc,'DATA DE NASCIMENTO': data_nasc, 'NÍVEL': nivel, 'LIMITAÇÕES': limit}
        lista_clientes.append(cliente)
        resp = str(input('Pretende continuar? (S/N)')).upper().strip()
        if resp == 'N':
            break
    return lista_clientes

def modificar(lst):
    #questao == 'S'
    while True:
        nome = (input('Selecione o nome do desportista: '))
        for desp in lst:
            for k,v in desp.items():
                if nome == v:
                        resp = input(f'Nome\n-Nº telemovel:\n-Morada\n-Cartão de cidadão\n- Data de nascimento\nNivel\nLimitações\nOlá {v}, que informação pretende alterar? ')
                        
                        if resp in desp:
                                altera = input(f'{resp}: ')
                                desp.update({resp: altera}) 
                                print(f'\nAlteração bem sucedida!\n{desp}')
                                break 
                                
                        else:
                            print('Reposta inválida')
                            break
                            

            if nome != v:
                print('Atleta não encontrado.\nCertifique-se que escreveu o nome corretamente (Nome e Apelido).')
        questao = input('Pretende continuar? [S/N]').upper().strip()
        if questao == 'N':
            break
