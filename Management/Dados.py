from Repetitive_actions.support_functions import *

def arquivoExiste(txt):
    try:
        a = open(txt, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(txt):
    try:
        a = open(txt, 'wt+') # w- write
        a.close()
    except:
        print('Houve um erro na criação do ficheiro.')
    else:
        print('Arquivo encontrado com sucesso!')


def lerArquivo(txt):
     try:
        a = open(txt, 'rt') #r read
     except:
         print('Erro ao ler o arquivo')
     else:
         linha()
         print('LISTA DAS PESSOAS'.center(35))
         print(a.read())
         linha()
     finally:
         a.close()

def adicionarDesportista(txt, lst):
    try:
        a = open(txt, 'at') #a -append
    except:
        print('Erro ao ler o arquivo.')
    else:
        try:
            for l in lst:
                a.write(f'{l}\n')
        except:
            print('Erro ao adicionar o(s) novo(s) elementos(s).')
        else:
            print('Novo(s) registo(s) guardados com sucesso')
    finally:
        a.close()