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


def adicionarDesportistas(txt, lst):
     
    try:
        key = 'ID'
        for item in lst:
            if key in item:
                del item[key] 
        # Tenta abrir e carregar os dados existentes do arquivo JSON
        try:
            with open(txt, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        except json.JSONDecodeError:
            data = []

        # Determina o próximo ID disponível
        if data:
            max_id = max(item["ID"] for item in data)
        else:
            max_id = 0

        # Atualiza os IDs dos novos desportistas e adiciona à lista existente
        for i, desportista in enumerate(lst):
            desportista["ID"] = max_id + i + 1
        data.extend(lst)

        # Escreve os dados atualizados de volta ao arquivo JSON
        with open(txt, 'w') as file:
            json.dump(data, file, indent=2)
        print('Novo(s) registro(s) guardados com sucesso')
    except Exception as e:
        print('Erro ao abrir ou escrever no arquivo.', e)

        


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