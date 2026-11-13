# ============================================================
# CAPÍTULO 4 — COLEÇÕES E SEQUÊNCIAS EM PYTHON
# EXERCÍCIOS PRÁTICOS | LOGIDATA
# ============================================================
#
# OBJETIVOS:
# - Trabalhar com dicionários, tuplas, arrays e range().
# - Aplicar validações e regras de negócio.
# - Desenvolver funções reutilizáveis.
# - Praticar processamento de dados.
#
# REGRAS:
# 1. Não utilizar pandas ou NumPy.
# 2. Consultar a documentação quando necessário.
# 3. Não modificar os dados originais, salvo quando solicitado.
# 4. Não utilizar soluções prontas de inteligência artificial.
# 5. Testar situações além dos exemplos fornecidos.
#
#
# ============================================================
# EXERCÍCIO 01 — DICIONÁRIOS
# CONTROLE DE ESTOQUE
# DIFICULDADE: INTERMEDIÁRIA
# ============================================================
#
# Uma transportadora possui um estoque de peças.
#
estoque = {
    "filtro": 15,
    "oleo": 8,
    "pneu": 20,
    "bateria": 4,
    "correia": 12
}


# Foram registradas as seguintes movimentações:
movimentacoes = [
    ("filtro", -3),
    ("oleo", 5),
    ("pneu", -8),
    ("bateria", -6),
    ("correia", 4),
    ("filtro", -5),
    ("lampada", 10)
]
# TAREFAS:
#
# 1. Crie uma função processar_estoque(estoque, movimentacoes).
# 2. Percorra todas as movimentações.
# 3. Atualize a quantidade dos produtos existentes.
# 4. Caso um produto não exista no estoque:
#    - Cadastre o produto com quantidade inicial zero.
#    - Processe sua movimentação.
# 5. Não permita que o estoque fique negativo.
#    Movimentações que causariam estoque negativo
#    devem ser rejeitadas integralmente.
# 6. Conte quantas movimentações foram rejeitadas.
# 7. Retorne o estoque atualizado e a quantidade
#    de movimentações rejeitadas.
# RESTRIÇÃO:
# Não modificar o dicionário original.
#
# DESAFIO:
# Como diferenciar uma movimentação de entrada
# de uma movimentação de saída?
def processar_estoque(estoque, movimentacoes):
    estoque_n = estoque.copy()
    reijeicoes = 0
    for item in movimentacoes:
        if item[0] in estoque_n:
            estoque_n[item[0]] += item[1]
            if estoque_n[item[0]] < 0:
                reijeicoes += 1
                estoque_n[item[0]] -= item[1]
        else:
            estoque_n[item[0]] = item[1]
    return estoque_n,reijeicoes

estoque_atualizado,rejeitos = processar_estoque(estoque,movimentacoes)
# print(f'Estoque atualizado : {estoque_atualizado}')
# print(f'Rejeitados: {rejeitos}')
# print(f'Estoque original: {estoque}')
# ============================================================
# EXERCÍCIO 02 — TUPLAS
# ANÁLISE DE ENTREGAS
# DIFICULDADE: INTERMEDIÁRIA
# ============================================================
#
# Cada tupla representa:
# (ID do pedido, cidade, dias de atraso)
#
entregas = [
    ("PED-001", "Campinas", 2),
    ("PED-002", "Santos", 0),
    ("PED-003", "São Paulo", 5),
    ("PED-004", "Campinas", 1),
    ("PED-005", "Jacareí", 0),
    ("PED-006", "Santos", 3),
    ("PED-007", "São Paulo", 7)
]


#
# TAREFAS:
#
# 1. Crie uma função analisar_entregas(entregas).
#
# 2. Conte quantas entregas tiveram atraso.
#
# 3. Calcule a média de dias de atraso,
#    considerando somente entregas atrasadas.
#
# 4. Identifique a entrega com maior atraso.
#
# 5. Crie uma nova lista de tuplas contendo
#    somente as entregas atrasadas.
#
# 6. Ordene essa nova lista pelo número de
#    dias de atraso, do maior para o menor.
#
# 7. Retorne os resultados da análise.
#
# DESAFIO:
# Como acessar individualmente os valores
# armazenados em cada tupla?
#

def analisar_entregas(entregas):
    lista_atrasados = []
    atrasos = 0
    soma_atrasos = 0

    for entrega in entregas:
        if entrega[2] > 0:
            atrasos += 1
            soma_atrasos += entrega[2]
            lista_atrasados.append(entrega)


    media_dias_atrasos = soma_atrasos / atrasos        
    lista_atrasados.sort(reverse=True,key=lambda x:x[2])
    entrega_maior_atraso = lista_atrasados[0]

    print('-=' * 30)
    print(f'Resultado da Análise\nLista de atrasos {lista_atrasados}\nTotal de atrasados {atrasos}\nMédia de dias de atraso {media_dias_atrasos}\nMaior dia de Atraso {entrega_maior_atraso}')
    print('-=' * 30)

analisar_entregas(entregas)
# ============================================================
# EXERCÍCIO 03 — ARRAYS
# PROCESSAMENTO DE TEMPERATURAS
# DIFICULDADE: INTERMEDIÁRIA
# ============================================================
#
from array import array

temperaturas = array(
    'i',
    [25, 28, 31, 35, 29, 40, 38, 22, 19, 34, 37, 26]
)
#
# Uma transportadora monitora a temperatura
# de um equipamento durante 12 medições.
#
# REGRAS:
# - Temperatura acima de 35 graus: alerta.
# - Temperatura abaixo de 20 graus: alerta.
# - Entre 20 e 35 graus: normal.
#
# TAREFAS:
#
# 1. Crie uma função analisar_temperaturas(temperaturas).
#
# 2. Calcule a temperatura média.
#
# 3. Identifique a maior e a menor temperatura.
#
# 4. Conte quantas medições geraram alertas.
#
# 5. Crie um novo array contendo somente
#    temperaturas consideradas normais.
#
# 6. Calcule a amplitude térmica:
#    maior temperatura - menor temperatura.
#
# 7. Retorne os resultados.
#
# RESTRIÇÃO:
# O array original deve permanecer inalterado.
#
# DESAFIO:
# Qual é a diferença entre armazenar esses
# valores em um array e em uma lista comum?
#
#
# ============================================================
# EXERCÍCIO 04 — RANGE()
# GERAÇÃO DE LOTES DE PROCESSAMENTO
# DIFICULDADE: INTERMEDIÁRIA / AVANÇADA
# ============================================================
#
# Uma transportadora precisa organizar pedidos
# em lotes para processamento.
#
# Os pedidos possuem IDs numéricos de 1001 até 1050.
#
# Cada lote deverá conter no máximo 7 pedidos.
#
# TAREFAS:
#
# 1. Crie uma função gerar_lotes(inicio, fim, tamanho_lote).
#
# 2. Gere os IDs dos pedidos utilizando range().
#
# 3. Divida os IDs em lotes com até 7 pedidos.
#
# 4. Armazene cada lote em uma lista.
#
# 5. Armazene todos os lotes em uma lista principal.
#
# 6. Retorne a lista principal.
#
# 7. Exiba a quantidade total de lotes.
#
# REGRAS:
# - O intervalo deve incluir inicio e fim.
# - Nenhum pedido pode ser repetido.
# - Nenhum pedido pode ser ignorado.
# - O último lote pode ter menos de 7 pedidos.
# - O tamanho_lote deve ser maior que zero.
#
# EXEMPLO SIMPLIFICADO:
#
# Entrada:
# inicio = 1
# fim = 10
# tamanho_lote = 3
#
# Saída esperada:
#
# [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [10]
# ]
#
# DESAFIOS:
#
# - Como utilizar o step do range() nesse problema?
# - Como evitar ultrapassar o último ID?
# - Como garantir que nenhum pedido seja perdido?
#
#
# ============================================================
# FIM DOS EXERCÍCIOS
# ============================================================