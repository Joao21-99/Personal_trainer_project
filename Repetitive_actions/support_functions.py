def menu(lista):
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    opcao = readInt('Opção: ')
    return opcao

def linha():
    print('*'*20)
    
def linha2():
    print('-'*20)

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
            

def readInt (txt):
    while True:
        try:
            msg = int(input(txt))
            return msg
        except(ValueError, TypeError):
            print('Esta categoria apenas aceita numeros inteiros.')
        except(KeyboardInterrupt):
            print('Execução interrompida.')
        continue

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
            num = int(num)
            break
        else:
            print(f'Esta categoria deve ter {l} algarismos.')
            num = input('Tente de novo: ')
    return num

def validateLevel():
    while True:
        print('Escolha o nível em que se econtra.')
        resposta = menu(['BÁSICO', 'MÉDIO', 'AVANÇADO','PROFISSIONAL'])

        if resposta == 1:
            return 'BÁSICO'
        elif resposta == 2:
           return 'MÉDIO'
        elif resposta == 3:
            return 'AVANÇADO' 
        elif resposta == 4:
            return 'PROFISSIONAL'
        else:
            print('Opcão inválida')
            linha2()

