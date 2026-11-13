# ============================================================
# CAPÍTULO 4 — LISTAS EM PYTHON
# EXERCÍCIOS PRÁTICOS | LOGIDATA
# ============================================================
#
# OBJETIVOS:
# - Manipular listas com autonomia.
# - Trabalhar com índices e fatiamento.
# - Inserir, remover e atualizar elementos.
# - Percorrer listas utilizando for e while.
# - Trabalhar com listas aninhadas.
# - Utilizar funções para organizar o processamento.
# - Desenvolver raciocínio aplicado a dados.
#
# REGRAS:
# 1. Não utilizar pandas, NumPy ou bibliotecas externas.
# 2. Consultar a documentação oficial quando necessário.
# 3. Não modificar os dados originais, exceto quando solicitado.
# 4. Criar funções quando o exercício exigir.
# 5. Testar situações diferentes das fornecidas.
#
# ============================================================
# EXERCÍCIO 01 — GERENCIAMENTO DE PEDIDOS
# DIFICULDADE: FÁCIL
# ============================================================
#
# Uma transportadora possui a seguinte lista:
#
pedidos = ["PED-001", "PED-002", "PED-003", "PED-004"]
#
# TAREFAS:
#
# 1. Adicione "PED-005" ao final da lista.
# 2. Insira "PED-000" na primeira posição.
# 3. Remova "PED-003" utilizando seu valor.
# 4. Remova o último pedido utilizando seu índice.
# 5. Verifique se "PED-002" está presente na lista.
# 6. Descubra a posição de "PED-004".
# 7. Exiba a quantidade de pedidos restantes.
#
# DESAFIO:
# Qual a diferença entre remove() e pop()?
# Remove remove primeira ocorrencia do valor, pop por default remove o ultimo elemento
# O que acontece se tentar remover um pedido inexistente?
# index error
pedidos.append("PED-005")
pedidos.insert(0,"PED-000")
pedidos.remove("PED-003")
pedidos.pop(-1)

print(pedidos.index("PED-002"))
print(pedidos.index("PED-004"))
print(f'Quantidade restantes: {len(pedidos)}')


# ============================================================
# EXERCÍCIO 02 — ANÁLISE DE FRETES
# DIFICULDADE: FÁCIL / INTERMEDIÁRIA
# ============================================================
#
fretes = [350, 780, 120, 500, 890, 250, 450, 620]
#
# TAREFAS:
#
# 1. Descubra o maior e o menor frete.
# 2. Calcule o valor total dos fretes.
# 3. Calcule a média dos fretes.
# 4. Crie uma nova lista contendo apenas fretes acima da média.
# 5. Ordene os fretes em ordem crescente.
# 6. Inverta a ordem dos elementos.
#
# DESAFIOS:
#
# - Qual a diferença entre sort() e sorted()?
# - Como ordenar sem modificar a lista original?
# criando uma copia da original
# - Quantos fretes estão acima da média?
# 4 fretes

menor_valor = min(fretes)
maior_valor = max(fretes)
valor_total_fretes = sum(fretes)
total_fretes = len(fretes)
media = valor_total_fretes / total_fretes
fretes_novo = []

print(f'Menor Valor: {menor_valor}')
print(f'Maior Valor: {maior_valor}')
print(f'Valor Total Frete: {valor_total_fretes}')
print(f'Quantidade Total Frete: {total_fretes}')
print(f'Media Frete: {media}\n')
for frete in fretes:
    if frete > media:
        fretes_novo.append(frete)


fretes.sort() # do menor para o maior
print(fretes)
fretes.reverse()
print(fretes)
print(fretes_novo)
print(30 * '-=')
# ============================================================
# EXERCÍCIO 03 — ÍNDICES E FATIAMENTO
# DIFICULDADE: INTERMEDIÁRIA
# ============================================================
#
entregas = [
    "São Paulo",
    "Campinas",
    "Santos",
    "Sorocaba",
    "Taubaté",
    "Jacareí",
    "Guarulhos",
    "Osasco"
]
#
# TAREFAS:
#
# 1. Exiba os três primeiros destinos.
# 2. Exiba os três últimos destinos.
# 3. Exiba os destinos das posições 2 até 5,
#    incluindo a posição 5.
# 4. Exiba os destinos em ordem inversa usando slicing.
# 5. Exiba apenas os destinos de índices pares.
# 6. Crie uma nova lista contendo os destinos
#    entre Campinas e Jacareí, incluindo ambos.
#
# DESAFIOS:
#
# - Qual a diferença entre entregas[-1] e entregas[:-1]?
# -1 pega a ultima ocorrencia e :-1 vai do index 0 até a ultima não incluso
# - O índice final de um slicing é incluído?
#não
# - O que representa o terceiro argumento do slicing?
# os passos
# print(entregas[0:3])
# print(entregas[-3:])
# print(entregas[2:6])
# print(entregas[::-1])
# print(entregas[::2])
# print(entregas[-1])
# print(entregas[:-1])
# entregas_nova = entregas[entregas.index('Campinas'):entregas.index('Jacareí')+1]




# ============================================================
# EXERCÍCIO 04 — LIMPEZA DE DADOS
# DIFICULDADE: INTERMEDIÁRIA
# ============================================================
#
cidades = [
    " São Paulo ",
    "CAMPINAS",
    "santos",
    "São Paulo",
    "  ",
    "Jacareí",
    "campinas",
    "",
    "Taubaté"
]
#
# TAREFAS:
#
# Crie uma função chamada limpar_cidades(lista).
#
# Ela deverá:
#
# 1. Remover espaços desnecessários.
# 2. Padronizar os nomes das cidades.
# 3. Ignorar strings vazias ou contendo apenas espaços.
# 4. Eliminar cidades duplicadas.
# 5. Retornar uma nova lista com as cidades válidas.
# 6. Preservar a ordem da primeira ocorrência.
#
# RESTRIÇÕES:
#
# - Não utilizar set().
# - Não alterar a lista original.
#
# DESAFIOS:
#
# - Como identificar duplicatas sem utilizar set()?
# - Por que padronizar antes de verificar duplicatas?
def limpar_cidades(lista):
    # nova lista
    lista_tratada = []

    # laço para percorrer lista passada como argumento
    for item in lista:
        if item.strip() == '':
            continue
        else:
            lista_tratada.append(item.strip().capitalize())

    lista_tratada_2 = []

    for i in lista_tratada:
        if i not in lista_tratada_2:
            lista_tratada_2.append(i)
    return lista_tratada_2

    # laço para percorrer a nova lista e remover duplicatas
    # for i in lista_tratada:
    #    if lista_tratada.count(i) == 2:
    #        lista_tratada.pop()

    
           
    

lista_tratada = limpar_cidades(cidades)
print(lista_tratada)
# ============================================================
# EXERCÍCIO 05 — LISTAS ANINHADAS
# DIFICULDADE: INTERMEDIÁRIA
# ============================================================
#
pedidos_logistica = [
    ["PED-001", "ENTREGUE", 350.00],
    ["PED-002", "PENDENTE", 780.50],
    ["PED-003", "ENTREGUE", 120.00],
    ["PED-004", "CANCELADO", 500.00],
    ["PED-005", "ENTREGUE", 890.00],
    ["PED-006", "PENDENTE", 250.00]
]


# APRENDIZADO, O SORTED NÃO MODIFICA A LISTA, RETORNA UMA NOVA

#
# TAREFAS:
#
# 1. Percorra todos os pedidos.
# 2. Conte quantos pedidos existem por status.
# 3. Calcule o faturamento dos pedidos entregues.
# 4. Descubra qual pedido entregue possui o maior valor.
# 5. Crie uma nova lista contendo somente pedidos pendentes.
# 6. Ordene os pedidos pelo valor do frete,
#    do maior para o menor.
#
# DESAFIOS:
#
# - Como acessar o valor de um pedido específico?
# - Como ordenar uma lista de listas pelo terceiro elemento?
# - É possível resolver sem alterar a lista original?
def ped_logistica(lista):
    entregue = 0
    pendente = 0
    cancelado = 0
    faturamento = 0
    maior_faturamento = 0
    lista_pendentes = []
    
    for item in lista:
        pedido = item[0].strip()
        status = item[1].strip()
        valor = float(item[2])

        if status == 'PENDENTE':
            pendente += 1
            lista_pendentes.append(item)
        elif status == 'ENTREGUE':
            entregue += 1
            faturamento += valor
            maior_faturamento = valor
            if valor > maior_faturamento:
                maior_faturamento = valor
        else:
            cancelado += 1
    print(entregue)
    print(faturamento)
    print(maior_faturamento)
    print(lista_pendentes)
    
ped_logistica(pedidos_logistica)

nova_ordem_pedidos_logistica = sorted(pedidos_logistica, key= lambda x: x[2], reverse=True)

print("--- ORDENADO POR MAIOR VALOR ---")
for i in nova_ordem_pedidos_logistica: print(i)

# ============================================================
# EXERCÍCIO 06 — REMOÇÃO SEGURA DE ELEMENTOS
# DIFICULDADE: INTERMEDIÁRIA / AVANÇADA
# ============================================================
#
# valores = [350, -100, 780, 0, 120, -50, 890, 0, 250]
valores = [350, -100, 0, -50, 780, 120]
#
# TAREFAS:
#
# 1. Identifique todos os valores menores ou iguais a zero.
# 2. Remova esses valores da lista utilizando pop().
# 3. Utilize while em sua implementação.
# 4. Não pule elementos durante as remoções.
# 5. Exiba a lista final.
#
# RESULTADO ESPERADO:
#
# [350, 780, 120, 890, 250]
#
# DESAFIOS:
#
# - Por que remover elementos enquanto percorremos
#   uma lista pode causar problemas?
# - Como controlar corretamente o índice do while?
# - Seria possível percorrer a lista de trás para frente?

c = 0
while c < len(valores):
    
    if valores[c] <= 0:
        valores.pop(c)

    else:
        c+=1
        continue
print(valores)
# ============================================================
# EXERCÍCIO 07 — MINI PROJETO: LOGIDATA V3
# DIFICULDADE: DESAFIO FINAL
# ============================================================
#
# Uma transportadora recebe dados de pedidos contendo:
# ID, status, valor e cidade.
#
registros = [
    ["PED-001", "ENTREGUE", 350.00, "São Paulo"],
    ["PED-002", "PENDENTE", 780.50, "Campinas"],
    ["PED-003", "ENTREGUE", 120.00, "Santos"],
    ["PED-004", "CANCELADO", 500.00, "Sorocaba"],
    ["PED-005", "ENTREGUE", -100.00, "Taubaté"],
    ["PED-006", "ENTREGUE", 890.00, "São Paulo"],
    ["PED-007", "DESCONHECIDO", 300.00, "Osasco"],
    ["PED-008", "PENDENTE", 0, "Jacareí"],
    ["PED-009", "ENTREGUE", 450.00, "Campinas"],
    ["PED-010", "PENDENTE", 620.00, "Guarulhos"]
]
#
# OBJETIVO:
#
# Construir um pequeno programa para analisar os pedidos.
#
# ETAPA 1 — VALIDAÇÃO
#
# 1. Identificar registros com valores menores ou iguais a zero.
# 2. Identificar registros com status desconhecido.
# 3. Separar registros válidos e inválidos em listas diferentes.
# 4. Preservar a lista original.
#
# ETAPA 2 — PROCESSAMENTO
#
# 5. Contar pedidos válidos por status.
# 6. Calcular o faturamento dos pedidos entregues.
# 7. Calcular o ticket médio dos pedidos entregues.
# 8. Identificar o pedido entregue de maior valor.
#
# ETAPA 3 — ORGANIZAÇÃO
#
# 9. Criar uma lista somente com pedidos entregues.
# 10. Ordenar essa lista pelo valor, em ordem decrescente.
# 11. Identificar as cidades que possuem entregas.
# 12. Remover cidades duplicadas, preservando a ordem.
#
# ETAPA 4 — FUNÇÕES
#
# Organize sua solução utilizando pelo menos três funções:
#
# - Uma para validar registros.
# - Uma para processar os pedidos.
# - Uma para apresentar os resultados.
#
# DESAFIO EXTRA:
#
# Faça o programa funcionar com outra lista de pedidos,
# sem precisar modificar o código das funções.
#
#
# ============================================================
# FIM DOS EXERCÍCIOS
# ============================================================
#
# REVISÃO:
#
# Ao concluir, você deverá conseguir explicar:
#
# - Quando utilizar append(), insert() e extend().
# - Diferenças entre remove(), pop() e del.
# - Como funcionam índices positivos e negativos.
# - Como funciona slicing.
# - Diferenças entre sort() e sorted().
# - Como manipular listas aninhadas.
# - Como evitar problemas ao remover elementos.
# - Como criar funções reutilizáveis para processar listas.
#
# ============================================================