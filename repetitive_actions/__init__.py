def errorString(a):
    a = a.replace(" ", "")
    while True:
        if a.isalpha():
            break
        else:
            print('Resposta inválida. Não se aceitam números nesta categoria.')
            a = input('Tente outra vez: ')
            a = a.replace(" ", "")

def errorNumeric(num):
    while True:
        if num.isnumeric():
            valor = int(num)
            break
        else:
            print('Resposta inválida. Não se aceitam letras nesta categoria.')
            num = input('Tente outra vez: ')

def errorDate():
    from datetime import datetime
    while True:
            data_nasc = input("Data de nascimento (formato: dd/mm/aaaa): ")
            try:
                data = datetime.strptime(data_nasc, "%d/%m/%Y")
                break  
            except ValueError:
                print("Formato de data inválido. Tente novamente.")
    return data_nasc



