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

        cliente = {'Nome': nome, 'Nº telefone': num_tel, 'Morada': morada, 'Cartão de cidadão':cc, 'Nível': nivel, 'Limitações': limit}
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
                if nome == v:
                    resp = input(f'Olá {v}, em breve conseguiremos alterar os seus dados.')
        if nome not in desp:
            print('Atleta não encontrado.\nCertifique-se que escreveu o nome corretamente.')
        questao = input('Pretende continuar? [S/N]').upper().strip()
        if questao == 'N':
            break
