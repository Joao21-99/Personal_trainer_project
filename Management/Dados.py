from Repetitive_actions.support_functions import *
import json

def arquivoExiste(file):
    try:
        a = open(file, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(file):
    try:
        a = open(file, 'wt+') # w- write
        a.close()
    except:
        print('Houve um erro na criação do ficheiro.')
    else:
        print('Arquivo encontrado com sucesso!')


def lerArquivo(file):
     try:
        a = open(file, 'rt') #r read
     except:
         print('Erro ao ler o arquivo')
     else:
         linha()
         print('LISTA DAS PESSOAS'.center(35))
         print(a.read())
         linha()
     finally:
         a.close()

def adicionarDesportistas(file, lst):  
    try:
        a = open(file, 'at') #a -append
        try:
            json.dump(lst, a, indent=2)
            a.write('\n')
        except Exception as err:
            print('Erro ao adicionar o(s) novo(s) elementos(s).', err)
        else:
            print('Novo(s) registo(s) guardados com sucesso')
        finally:
         a.close() 
    except Exception as e:
         print('Erro ao ler o arquivo.', e)


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