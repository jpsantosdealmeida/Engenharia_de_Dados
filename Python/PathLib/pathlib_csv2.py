from pathlib import Path
import csv
import logging

# Definindo log
logger = logging.getLogger(__name__)
logging.basicConfig(filename='exemplo.log', encoding='utf-8', level=logging.DEBUG)

# Definindo caminho arquivos

caminho_csv_items = Path.cwd() / 'Projetos' / 'dados' / 'olist_order_items_dataset.csv'

caminho_csv_pagamentos = Path.cwd() / 'Projetos' / 'dados' / 'olist_order_payments_dataset.csv'

caminho_csv_pedidos = Path.cwd() / 'Projetos' / 'dados' / 'olist_orders_dataset.csv'

def step1_exploracao(caminho):
    with open(caminho,'r',encoding='utf-8',newline='') as arq:
        leitor = csv.DictReader(arq)
        cabecalho = leitor.fieldnames
        contador = 0

        lista_registros = []
        total_linhas = 0
        for linha in leitor:

            if contador < 5:
                lista_registros.append(linha)
                contador += 1
            total_linhas += 1
        return lista_registros,cabecalho,total_linhas

csv_items,cabecalho_items,linhas_items = step1_exploracao(caminho_csv_items)
csv_pagamentos,cabecalho_pagamentos,linhas_pagamentos = step1_exploracao(caminho_csv_pagamentos)
csv_pedidos,cabecalho_pedidos,linhas_pedidos = step1_exploracao(caminho_csv_pedidos)

def step1_verif_relacionamentos(*args):
    lista_unificada = []
    
    for cabecalho in args:
        for coluna in cabecalho:
            lista_unificada.append(coluna)

    lista_chaves_relacionamentos = []

    for i,item in enumerate(lista_unificada,0):
        if lista_unificada.count(item) == len(args):
            lista_chaves_relacionamentos.append(item)
            

    return lista_chaves_relacionamentos

    

a = step1_verif_relacionamentos(cabecalho_items,cabecalho_pagamentos,cabecalho_pedidos)
print(a)
# pseudocodigo
'''
recebe args

faz uma copia com uma lista só 
verifica qual tem 3 registros
e deixa 1 dos 3 registros

'''

