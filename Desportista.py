def novo():
    from datetime import datetime
    cliente = []
    lista_clientes = []
    nome = input('Nome: ').strip()
    cliente.append(nome)
    num_tel = int(input('Nº telemovel: '))
    cliente.append(num_tel)
    morada = input('Morada: ').strip()
    cliente.append(morada)
    cc = int(input('cartão de cidadão: '))
    cliente.append(cc)
    while True:
        data_nasc = input("Digite sua data de nascimento (formato: dd/mm/aaaa): ")
        try:
            data = datetime.strptime(data_nasc, "%d/%m/%Y")
            break  
        except ValueError:
            print("Formato de data inválido. Tente novamente.")
    nivel = input('Nível: ')
    cliente.append(nivel)
    limit = input('Limitações: ')
    cliente.append(limit)
    lista_clientes.append(cliente)
    print('Dados carregados com sucesso!')
    print(cliente)
    print(lista_clientes)
