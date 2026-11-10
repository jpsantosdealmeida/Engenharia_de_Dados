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
        leitor = csv.reader(arq)
        cabecalho = next(leitor)
        contador = 0
        lista_registros = []

        # retornando 5 primeiras linhas
        caminho.read
        # for x in range(0,5):
        #     leitor = list(leitor)
        #     lista_registros.append(leitor[x])

        # # total linhas
        # total_linhas = len(list(leitor))
        
        # return lista_registros,cabecalho,total_linhas
       
                
        

csv_items,cabecalho_items,total_linha_items = step1_exploracao(caminho_csv_items)
csv_pagamentos,cabecalho_pagamentos,total_linha_pagamentos = step1_exploracao(caminho_csv_pagamentos)
csv_pedidos,cabecalho_pedidos,total_linha_pedidos = step1_exploracao(caminho_csv_pedidos)


