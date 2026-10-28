# ============================================================
# PYTHON — DIA 02
# REVISÃO INTEGRADA | 6 EXERCÍCIOS
# ============================================================

import random

# ============================================================
# EXERCÍCIO 01 — TRATAMENTO DE CADASTROS
# NÍVEL: INTERMEDIÁRIO
# ============================================================
#
# Um sistema recebeu os dados de um cliente em uma única
# string, separados pelo caractere ";".
#
# TAREFAS: 
# 1. Remova os espaços desnecessários de cada campo.
# 2. Transforme o nome em letras maiúsculas.
# 3. Transforme o e-mail em letras minúsculas.
# 4. Extraia a cidade sem depender do nome dela.
# 5. Monte uma identificação usando join().
# 6. Exiba a quantidade de caracteres do nome tratado.
#
# RESULTADO ESPERADO:
#
# Cliente: MARIA OLIVEIRA
# E-mail: maria@email.com
# Cidade: São José dos Campos
# Identificação: MARIA OLIVEIRA | São José dos Campos
# Caracteres no nome: 14
#
# TESTE EXTRA:
# Troque os dados por outro cliente e verifique se a
# lógica continua funcionando.
# ============================================================
cadastro = "  maria oliveira ; MARIA@EMAIL.COM ; São José dos Campos  " # Testei com outro nome,email e cidade e funcionou a lógica.
# SUA SOLUÇÃO:
nome = cadastro.split(';')[0].upper().strip()
email = cadastro.split(';')[1].lower().strip()
cidade = cadastro.split(';')[2].strip()
ident = [nome,cidade]
print(f'''
Cliente: {nome}
E-mail: {email}
Cidade: {cidade}
Identificação: {' | '.join(ident)}
Caracteres no nome: {len(nome)}
''')
# ============================================================
# EXERCÍCIO 02 — SIMULADOR DE PEDIDOS
# NÍVEL: INTERMEDIÁRIO
# ============================================================
#
# Um cliente está realizando uma compra.
#
# TAREFAS:
# 1. Solicite o nome do cliente usando input().
# 2. Solicite o valor unitário de um produto.
# 3. Solicite a quantidade comprada.
# 4. Calcule o valor total.
# 5. Aplique 10% de desconto se o total for maior
#    ou igual a R$ 200,00.
# 6. Gere um número aleatório de pedido entre 1000 e 9999.
# 7. Apresente um resumo da compra.
#
# EXEMPLO:
#
# Nome: João
# Valor unitário: 50
# Quantidade: 5
#
# RESULTADO ESPERADO:
#
# Pedido: [número aleatório]
# Cliente: JOÃO
# Subtotal: R$ 250.00
# Desconto: R$ 25.00
# Total: R$ 225.00
#
# TESTES OBRIGATÓRIOS:
# - Uma compra abaixo de R$ 200.
# - Uma compra exatamente de R$ 200.
# - Uma compra acima de R$ 200.
#
# ============================================================

# SUA SOLUÇÃO:
# print(30*'=')
# import random
# nome_cliente = input('Insira seu nome: ').upper()
# valor_produto = float(input('Valor do produto: '))
# quantidade = int(input('Quantidade comprada: '))
# subtotal = float(quantidade * valor_produto)
# numero_pedido = random.randint(1000,9999)

# if subtotal >= 200:
#     valor_total = round(subtotal * 0.9,2)
#     desconto = round(subtotal * 0.1,2)
#     print(f'''
#         Pedido: {numero_pedido}
#         Cliente: {nome_cliente}
#         Subtotal: R$ {subtotal}
#         Desconto: R$ {desconto}
#         Total: R$ {valor_total}
#         ''')
# else:
#     print(f'''
#         Pedido: {numero_pedido}
#         Cliente: {nome_cliente}
#         Subtotal: R$ {subtotal}
#         Desconto: R$ 0.00
#         Total: R$ {subtotal}
#         ''')

# ============================================================
# EXERCÍCIO 03 — PRAZO DE ENTREGA
# NÍVEL: INTERMEDIÁRIO
# ============================================================
#
# Uma transportadora precisa calcular o prazo de entrega
# de um pedido.
#
# TAREFAS:
# 1. Receba uma data de postagem via input().
# 2. A data será informada no formato DD/MM/AAAA.
# 3. Converta a entrada para um objeto datetime.
# 4. Solicite o prazo de entrega em dias.
# 5. Calcule a data prevista de entrega.
# 6. Compare a previsão com a data atual.
# 7. Informe se a entrega está prevista para o futuro,
#    para hoje ou se a data prevista já passou.
#
# EXEMPLO:
#
# Data de postagem: 20/10/2026
# Prazo: 5 dias
#
# RESULTADO ESPERADO:
#
# Data prevista: 25/10/2026
# Situação: [calculada conforme a data atual]
#
# DICAS:
# - Pesquise sobre timedelta na documentação do Python.
# - Para comparar apenas datas, investigue .date().
#
# REGRA:
# Considere dias corridos, não dias úteis.
#
# ============================================================
# SUA SOLUÇÃO:

# print(30 * '=')
# from datetime import datetime, timedelta
# data_postagem = datetime.strptime(input('Data da Postagem: '),'%d/%m/%Y')
# prazo_entrega = int(input('Prazo de entrega (dias): '))
# data_prevista = data_postagem + timedelta(days=prazo_entrega)
# data_prevista_formatada = data_prevista.strftime('%d/%m/%Y')

# hoje = datetime.now().date()

# if data_prevista.date() < hoje:
#     situacao = 'Entrega já passou'
# elif data_prevista.date() == hoje:
#     situacao = 'Entrega prevista para hoje'
# else:
#     situacao = 'Entrega para o futuro'

# print(f'''
# Data de postagem: {data_postagem.date()}
# Prazo: {prazo_entrega} 

# Data prevista: {data_prevista_formatada}
# Situação: {situacao}


# # ''')

# print(30 * '=')

# ============================================================
# EXERCÍCIO 04 — SORTEIO DE ENTREGAS
# NÍVEL: INTERMEDIÁRIO / DESAFIADOR
# ============================================================
#
# Uma transportadora possui cinco entregas disponíveis.
# O sistema precisa selecionar aleatoriamente três delas.
#
# TAREFAS:
# 1. Sorteie três pedidos diferentes.
# 2. Nenhum pedido pode aparecer repetido.
# 3. Apresente os pedidos selecionados.
# 4. Una os códigos sorteados em uma única string,
#    separados por " | ".
# 5. Exiba a quantidade de pedidos sorteados.
#
# EXEMPLO DE SAÍDA:
#
# Pedidos sorteados: ['PED-101', 'PED-104', 'PED-105']
# Resumo: PED-101 | PED-104 | PED-105
# Quantidade: 3
#
# ATENÇÃO:
# random.choices() permite elementos repetidos.
# Pesquise na documentação uma alternativa para
# selecionar elementos sem repetição.
#
# ============================================================

# pedidos = [
#     "PED-101",
#     "PED-102",
#     "PED-103",
#     "PED-104",
#     "PED-105"
# ]

# # SUA SOLUÇÃO:
# pedidos_sorteados = random.sample(pedidos,k=3)
# quantidade_sorteados = len(pedidos_sorteados)

# print(f'''
# Pedidos sorteados: {pedidos_sorteados}
# Resumo: {' | '.join(pedidos_sorteados)}
# Quantidade: {quantidade_sorteados}
# ''')


# ============================================================
# EXERCÍCIO 05 — VALIDAÇÃO DE REGISTROS
# NÍVEL: DESAFIADOR
# ============================================================
#
# Um sistema recebeu informações de um pedido.
#
# TAREFAS:
# 1. Separe os campos pelo caractere ";".
# 2. Remova os espaços desnecessários.
# 3. Padronize o status para letras minúsculas.
# 4. Converta o valor para float.
# 5. Verifique se o status é "pendente".
# 6. Verifique se o valor é maior que R$ 500.
# 7. Classifique o pedido:
#
#    - "ATENÇÃO": pendente e valor maior que R$ 500.
#    - "NORMAL": qualquer outra combinação.
#
# 8. Apresente o resultado usando f-strings.
#
# RESULTADO ESPERADO:
#
# Pedido: PED-2080
# Status: pendente
# Valor: R$ 750.00
# Classificação: ATENÇÃO
#
# TESTES EXTRAS:
#
# "PED-2081;ENTREGUE;900.00"
# "PED-2082;PENDENTE;250.00"
# "PED-2083;PENDENTE;500.00"
#
# IMPORTANTE:
# Observe a diferença entre > 500 e >= 500.
#
# ============================================================

registro = "  PED-2080 ; PENDENTE ; 750.00  "


# SUA SOLUÇÃO:
print(30 * '=')
registro_tratado = registro.strip()
pedido = registro.split(';')[0].strip()
status = registro.split(';')[1].strip().lower()
valor = float(registro.split(';')[2].strip())
classificacao = 'NORMAL'
# Verificando se o status é pendnete e valor > 500
if status == 'pendente' and valor > 500:
    classificacao = 'ATENÇÃO'
    print(f'''
        Pedido: {pedido}
        Status: {status}
        Valor: R$ {valor}
        Classificação: {classificacao}
    ''')
else:
    print(f'''
        Pedido: {pedido}
        Status: {status}
        Valor: R$ {valor}
        Classificação: {classificacao}
    ''')

# ============================================================
# EXERCÍCIO 06 — PROCESSAMENTO DE VENDAS
# NÍVEL: DESAFIADOR
# ============================================================
#
# Você recebeu uma lista com registros de vendas.
# Cada registro contém:
#
# DATA;PEDIDO;CLIENTE;VALOR
#
# TAREFAS:
# 1. Separe cada registro em campos.
# 2. Remova os espaços desnecessários.
# 3. Padronize os nomes dos clientes em maiúsculas.
# 4. Converta os valores para float.
# 5. Calcule o faturamento total.
# 6. Calcule o ticket médio das três vendas.
# 7. Identifique o pedido de maior valor.
# 8. Exiba um resumo das vendas.
#
# RESULTADO ESPERADO:
#
# Quantidade de vendas: 3
# Faturamento total: R$ 1000.00
# Ticket médio: R$ 333.33
# Maior venda: PED-003
# Valor da maior venda: R$ 500.00
#
# DESAFIO EXTRA:
# Exiba também a data da venda mais recente.
#
# REGRAS:
# - Não escreva manualmente os resultados.
# - Utilize apenas os conteúdos estudados.
# - Se ainda não estudou laços de repetição, pode
#   processar cada registro separadamente.
# - Não é necessário utilizar pandas.
#
# ============================================================

venda1 = "2026-10-18;PED-001;joão silva;200.00"
venda2 = "2026-10-19;PED-002;maria oliveira;300.00"
venda3 = "2026-10-20;PED-003;ana costa;500.00"
lista = [venda1,venda2,venda3]
# SUA SOLUÇÃO:

for index in range(len(lista)):
    lista[index].split(';')
    print(lista)
# ============================================================
# FIM DOS EXERCÍCIOS — DIA 02
# ============================================================
#
# REFLEXÃO FINAL:
#
# 1. Qual exercício exigiu mais raciocínio?
#
# 2. Em qual momento você precisou consultar
#    a documentação?
#
# 3. Qual conceito você percebeu que precisa revisar?
#
# 4. Você conseguiria explicar suas soluções
#    para outra pessoa?
#
# ============================================================
