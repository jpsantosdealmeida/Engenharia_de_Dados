from pathlib import Path
import csv
import logging
from collections import Counter
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

def step1_verif_relacionamentos(*cabecalhos):
    colecao = set()
    if len(cabecalhos) == 0:
        return colecao
    
    conjunto = set(cabecalhos[0])

    # Refatorando
    # for index in range(1,len(cabecalhos)):
    #     conjunto = conjunto.intersection(cabecalhos[index])

    for cabecalho in cabecalhos[1:]:
        conjunto = conjunto.intersection(cabecalho)
        

    return conjunto


# Exploração ( csv,cabeçalho e total de linhas)
csv_items,cabecalho_items,linhas_items = step1_exploracao(caminho_csv_items)
csv_pagamentos,cabecalho_pagamentos,linhas_pagamentos = step1_exploracao(caminho_csv_pagamentos)
csv_pedidos,cabecalho_pedidos,linhas_pedidos = step1_exploracao(caminho_csv_pedidos)

# Possíveis colunas de relação
relacionamentos = step1_verif_relacionamentos(cabecalho_items,cabecalho_pagamentos,cabecalho_pedidos)

def step2_exploracao_csv(caminho,coluna):
    contador = Counter()
    dicio_ids_repetidos = {}
    with open(caminho,'r',encoding='utf-8',newline='') as arq:
        
        
        leitor = csv.DictReader(arq)

        for linha in leitor:
            
            contador.update([linha[coluna]])
            
        total_registros = contador.total()
        total_registros_diferentes = len(contador)


        for chave,valor in contador.items():
            if valor > 1:
                dicio_ids_repetidos[chave] = valor

        order_ids_repetidos = len(dicio_ids_repetidos)
        total_registros_excedentes = total_registros - total_registros_diferentes

        print(f'Total de registros: {total_registros}')
        print(f'Total de order_id distintos: {total_registros_diferentes}')
        print(f'Quantidade de order_id repetidos: {order_ids_repetidos}')
        print(f'Quantidade de ocorrências excedentes: {total_registros_excedentes}')
    
        

step2_exploracao_csv(caminho_csv_pagamentos,relacionamentos.pop())

    


    


