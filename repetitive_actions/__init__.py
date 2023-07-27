def errorString(a):
    b = a.replace(" ", "")
    while True:
        if b.isalpha():
            break
        else:
            print('Resposta inválida. Não se aceitam números nesta categoria.')
            a = input('Tente outra vez: ')
            b = a.replace(" ", "")
    return a
            

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

def validateNumber(num, l):
    while True:
        if len(num) == l and num.isnumeric() == True:
            break
        else:
            print(f'Esta categoria deve ter {l} algarismos.')
            num = input('Tente de novo: ')
    return num

def validateLevel(msg):
    while True:
        if 'BÁSICO' in msg.upper():
            break
        elif 'MÉDIO' in msg.upper():
           break
        elif 'AVANÇADO' in msg.upper():
            break 
        elif 'PRO'in msg.upper():
            break
        else:
            msg = input('Opção inválida. Tente de novo: ')
    return msg