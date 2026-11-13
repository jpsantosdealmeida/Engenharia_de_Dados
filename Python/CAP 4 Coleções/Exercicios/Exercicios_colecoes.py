from operator import itemgetter
# ============================================================
# REVISAO DE PYTHON — LISTAS E COLECOES
# Exercicios sem solucoes | Contexto: e-commerce e catalogo
# ============================================================
# REGRAS:
# - Nao usar pandas, NumPy ou bibliotecas externas.
# - Consultar a documentacao oficial.
# - Nao modificar os dados originais, salvo indicacao expressa.
# - Escrever funcoes reutilizaveis quando solicitado.
# - Testar casos vazios, repetidos e limites.

# # EXERCICIO 01 — LISTAS, INDICES E ENUMERATE (FACIL)
produtos = ["teclado", "mouse", "monitor", "webcam", "headset"]
# # 1. Exiba cada produto com sua posicao, comecando a numeracao em 1.
tupla_exercicio_2 = []
for indice,produto in enumerate(produtos,1):
    print(f'Posição {indice} -> Produto { produto}')
    tupla_exercicio_2.append((indice,produto))


# # 2. Crie uma nova lista de tuplas (numero, produto) sem alterar a original.
print(tupla_exercicio_2)
# # 3. Encontre a posicao de "webcam" usando uma iteracao com enumerate().
# for posicao,produto in enumerate(produtos_tupla,0):
#     if produto == 'webcam':
#        print(f'Posição {posicao} -> Produto { produto}') 
# # 4. Mostre os tres ultimos produtos por slicing.
# print(produtos[-3:])
# # 5. Teste o que ocorre quando a lista esta vazia.
# produtos.clear()
# print(produtos[-3:])


# INVESTIGAR: enumerate(iterable, start=0), list(), slicing.

# EXERCICIO 02 — MAP: TRANSFORMACAO (INTERMEDIARIO)
precos_texto = [" 19.90 ", "35.50", " 100.00", "8.75 "]
# 1. Crie uma funcao converter_preco(texto) que remova espacos e converta para float.
def converter_preco(texto):
    return float(texto.strip())

# 2. Utilize map() para aplicar a funcao a todos os elementos.
precos_texto = list(map(converter_preco,precos_texto))

# 3. Materialize o resultado em uma lista e calcule o total.
total_precos_texto = (sum(precos_texto))
print(f'Total preços com sum: {total_precos_texto}')
# 4. Compare a abordagem com um for convencional.
soma = 0 
for item in precos_texto:
    soma += item
print(f'Total preços com for: {soma}')
# mesmo resultado

# EXERCICIO 03 — FILTER: SELECAO (INTERMEDIARIO)
estoque = [
    {"produto": "teclado", "quantidade": 8, "ativo": True},
    {"produto": "mouse", "quantidade": 0, "ativo": True},
    {"produto": "monitor", "quantidade": 3, "ativo": False},
    {"produto": "webcam", "quantidade": 5, "ativo": True},
    {"produto": "headset", "quantidade": -2, "ativo": True},
]
# 1. Selecione somente produtos ativos com quantidade maior que zero usando filter().
def selecao_ativos(colecao):
    if colecao['quantidade'] > 0 and colecao['ativo'] == True:
        # return colecao['produto']
        print(colecao['produto'])

# 2. Gere uma lista apenas com os nomes dos produtos selecionados.
list(filter(selecao_ativos,estoque))
# print(f'Lista Ativos: {lista_ativos}')
# 3. Compare filter() com um for + if.
for item in estoque:
    if item['quantidade'] > 0 and item['ativo'] == True:
        print(item)

# 4. Explique a diferenca entre transformar e filtrar dados.
'''
Transformar é deixar o dado do jeito que precisamos , seja por exemplo.. Maiusculos, inteiros 
já filtrar é retornar o dado dada algum condição que deve obedecer
'''



# EXERCICIO 04 — SETS E OPERACOES (INTERMEDIARIO)
clientes_janeiro = ["C01", "C02", "C03", "C03", "C05"]
clientes_fevereiro = ["C02", "C03", "C04", "C06", "C06"]
# 1. Identifique os clientes distintos de cada mes.
print(set(clientes_janeiro))
print(set(clientes_fevereiro))
# 2. Identifique clientes presentes nos dois meses.
print(set(clientes_janeiro).intersection(set(clientes_fevereiro)))
# 3. Identifique clientes que compraram apenas em janeiro.
print(set(clientes_janeiro).difference(set(clientes_fevereiro)))
# 4. Identifique todos os clientes que compraram em pelo menos um mes.
print(set(clientes_janeiro).union(set(clientes_fevereiro)))
# 5. Explique por que set nao garante preservar a ordem original.
'''
Tive que procurar mas é por conta da organização na memoria utilizando tabela hash

'''
# 6. Retorne uma lista ordenada dos clientes comuns.
clientes_comuns = list(set(clientes_janeiro).intersection(set(clientes_fevereiro)))
clientes_comuns.sort()
print(clientes_comuns)
# INVESTIGAR: set(), intersection(), difference(), union(), sorted().

# EXERCICIO 05 — ORDENACAO COM ITEMGETTER (INTERMEDIARIO)
vendas = [
    ("V01", "livros", 150.00),
    ("V02", "eletronicos", 900.00),
    ("V03", "livros", 150.00),
    ("V04", "casa", 320.00),
    ("V05", "eletronicos", 450.00),
]
# 1. Ordene as vendas por valor crescente usando sorted() e itemgetter().

from operator import itemgetter
print(f'Vendas: {vendas}')
print(f'Vendas Sorted: {sorted(vendas,key=lambda x:x[2])}')
vendas.sort(key=itemgetter(2))
print(f'Vendas Itemgetter: {vendas}')

# 2. Ordene por valor decrescente, preservando a lista original.

vendas.sort(key=itemgetter(2),reverse=True)
print(vendas)


# 3. Ordene por categoria e, em caso de empate, por valor.
vendas.sort(key=itemgetter(1,2))
print(vendas)

# 4. Compare itemgetter(2) com lambda registro: registro[2].


# 5. Explique o que acontece com elementos empatados na ordenacao.


# INVESTIGAR: from operator import itemgetter, sorted(), key, reverse, estabilidade.

# EXERCICIO 06 — LISTAS ANINHADAS E COMBINACOES (INTERMEDIARIO)
transacoes = [
    ["T01", "aprovado", 120.00, "livros"],
    ["T02", "recusado", 75.00, "casa"],
    ["T03", "aprovado", 310.00, "eletronicos"],
    ["T04", "aprovado", 120.00, "livros"],
    ["T05", "pendente", 50.00, "casa"],
]
# 1. Crie uma funcao que receba a lista de transacoes.
print(20 * '=-')
def analisar_transacoes(t):
    
    
    if t[1] == 'aprovado':
        return t[1]
        

# 2. Filtre apenas transacoes aprovadas.
        
transacoes_aprovadas = list(filter(analisar_transacoes,transacoes))
print(transacoes_aprovadas)

print(20 * '=-')
# 3. Transforme os registros aprovados em uma lista de (id, valor).
def lista_transacoes_aprovadas(aprovadas):
    lista_aprovadas = []
    for item in aprovadas:
        lista_aprovadas.append([item[0],item[2]])
    return lista_aprovadas

aprovadas = lista_transacoes_aprovadas(transacoes_aprovadas)
print(aprovadas)
print(20 * '=-')
# 4. Ordene o resultado pelo valor decrescente com itemgetter().
aprovadas.sort(key=itemgetter(1),reverse=True)
print(aprovadas)
print(20 * '=-')
# 5. Liste as categorias distintas das transacoes aprovadas usando set.
def cat_distintas(t):
     conj_cat = set()
     for item in t:
         conj_cat.add(item[3])
     return conj_cat
        
print(20 * '=-')
conjuntos_categoria = cat_distintas(transacoes_aprovadas)
print(conjuntos_categoria)
print(20 * '=-')

# 6. Exiba a posicao de cada transacao ordenada com enumerate(start=1).
for indice,transacao in enumerate(aprovadas,1):
    print(f'Posição transação {indice} | Transação {transacao}')

print(20 * '_-°-_')
# 7. Preserve transacoes e suas listas internas sem alteracoes.
# INVESTIGAR: filter(), map(), itemgetter(), set(), enumerate().

# EXERCICIO 07 — REMOCAO SEGURA E MUTABILIDADE (INTERMEDIARIO)
quantidades = [5, 0, -2, -1, 8, 0, 3]
# 1. Faca uma copia da lista original.
quantidades_copia = quantidades.copy()
# 2. Remova da copia os valores menores ou iguais a zero usando while e pop().
contador = 0
while contador < len(quantidades_copia):
    if quantidades_copia[contador] <= 0:
        quantidades_copia.pop(contador)
        continue
    else:
        contador += 1

    # Entendi aqui que no while só vou adicionar 1 quando não remover nada, tendo em vista que quando removemos deslocamos a esquerda

print(quantidades_copia)
print(20 * '-')
# 3. Nao pule valores invalidos consecutivos.
# 4. Resolva novamente criando uma nova lista com filter(), sem remover elementos.
quantidades_copia_2 = quantidades.copy()
def analise_lista(valor):
    if valor > 0:
        return True
    else:
        return False


print(list(filter(analise_lista,quantidades_copia_2)))

# 5. Compare os resultados e explique os efeitos sobre a lista original.
# INVESTIGAR: copy(), pop(), while, filter(), mutabilidade.

# EXERCICIO 08 — MINIPROJETO: ANALISE DE VENDAS (DESAFIO)
registros_vendas = [
    ["P001", "livros", 59.90, 2, "aprovado"],
    ["P002", "casa", 120.00, 1, "aprovado"],
    ["P003", "livros", -15.00, 1, "aprovado"],
    ["P004", "eletronicos", 800.00, 0, "pendente"],
    ["P005", "casa", 75.00, 3, "aprovado"],
    ["P006", "livros", 40.00, 1, "desconhecido"],
    ["P007", "eletronicos", 400.00, 2, "aprovado"],
    ["P008", "casa", 75.00, 1, "aprovado"],
]
# OBJETIVO: criar um relatorio de vendas sem modificar a origem.
# 1. Defina uma funcao para validar preco, quantidade e status.
# 2. Separe registros validos e invalidos, registrando o motivo da invalidade.
# 3. Calcule o faturamento dos registros aprovados (preco * quantidade).
# 4. Identifique as categorias distintas com set.
# 5. Gere uma lista de (id, valor_total) das vendas aprovadas.
# 6. Ordene-a por valor_total decrescente usando itemgetter().
# 7. Exiba um ranking numerado usando enumerate(start=1).
# 8. Utilize map() ou filter() em pelo menos uma etapa e justifique a escolha.
# 9. Organize a solucao em pelo menos tres funcoes reutilizaveis.
# 10. Teste com registros vazios, invalidos e valores empatados.
# DESAFIO EXTRA: apresente uma versao usando for e outra usando map/filter
# em uma etapa escolhida; compare legibilidade e comportamento.
# ============================================================
