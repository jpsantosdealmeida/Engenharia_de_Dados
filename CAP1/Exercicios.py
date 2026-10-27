
# ============================================================
# PYTHON — DIA 01
# REVISÃO: STRINGS, VARIÁVEIS E TIPOS PRIMITIVOS
# ============================================================
#
# Conteúdos:
# - Variáveis e tipos primitivos
# - Strings e f-strings
# - Indexação e slicing
# - strip(), lower(), upper(), replace()
# - find(), index(), rindex(), len()
# - split()
#
# Objetivo:
# Resolver os exercícios utilizando os conteúdos estudados.
# Evite consultar soluções prontas.
#
# ============================================================


# ============================================================
# EXERCÍCIO 01 — LIMPEZA DE DADOS
# NÍVEL: FÁCIL
# ============================================================
#
# Um sistema recebeu o nome de um cliente com espaços
# desnecessários e letras misturadas.
#
# TAREFAS:
# 1. Remova os espaços no início e no final.
# 2. Transforme todas as letras em maiúsculas.
# 3. Descubra a quantidade de caracteres do nome tratado.
# 4. Apresente os resultados usando f-strings.
#
# RESULTADO ESPERADO:
#
# Nome tratado: JOÃO PAULO
# Quantidade de caracteres: 10
#
# REGRAS:
# - Não altere manualmente o conteúdo da variável.
# - Utilize métodos de string.
#
# ============================================================

cliente = "   jOÃO pAULO   "


# ESCREVA SUA SOLUÇÃO ABAIXO:
print(f'O nome {cliente.strip().upper()} possuí {len(cliente.strip())} caracteres.')




# ============================================================
# EXERCÍCIO 02 — EXTRAÇÃO DE INFORMAÇÕES
# NÍVEL: FÁCIL
# ============================================================
#
# Uma transportadora utiliza códigos padronizados
# para identificar suas entregas.
#
# TAREFAS:
# 1. Extraia o código do país.
# 2. Extraia o estado.
# 3. Extraia o ano.
# 4. Extraia o identificador da entrega.
#
# RESULTADO ESPERADO:
#
# País: BR
# Estado: SP
# Ano: 2026
# Identificador: 000145
#
# REGRAS:
# - Utilize slicing, indexação ou split().
# - Não escreva os resultados manualmente.
# - Preserve os zeros do identificador.
#
# ============================================================

codigo = "BR-SP-2026-000145"



# ESCREVA SUA SOLUÇÃO ABAIXO:
print(f'País: {codigo.split('-')[0]}\nEstado: {codigo.split('-')[1]}\nAno: {codigo.split('-')[2]}\nIdentificador: {codigo.split('-')[3]}')



# ============================================================
# EXERCÍCIO 03 — LOCALIZANDO INFORMAÇÕES
# NÍVEL: INTERMEDIÁRIO
# ============================================================
#
# Uma transportadora registrou uma mensagem de entrega.
#
# TAREFAS:
# 1. Encontre a posição inicial da palavra "Pedido".
# 2. Encontre a posição inicial da palavra "Entrega".
# 3. Extraia somente o número do pedido.
# 4. Extraia somente o nome da cidade.
# 5. Verifique se a palavra "pendente" existe na mensagem.
#
# RESULTADO ESPERADO:
#
# Posição de Pedido: 0
# Número do pedido: 4587
# Cidade: São Paulo
# Pendente encontrado: True
#
# REGRAS:
# - Utilize os métodos de string estudados.
# - Não escreva manualmente os valores extraídos.
# - A posição de "Entrega" também deve ser apresentada.
#
# ============================================================

mensagem = "Pedido 4587 enviado para São Paulo - Entrega pendente"

# ESCREVA SUA SOLUÇÃO ABAIXO:
print(20 * '-=')
print(f'Posição Inicial da palavra Entrega: {mensagem.find('Entrega')}')
print(f'Posição de Pedido: {mensagem.find('Pedido')}')
# print(f'Número do pedido: {mensagem[mensagem.index('4'):mensagem.index('7')+1]}') tinha feito assim agora fiz do jeito abaixo
print(f'Número do pedido: {mensagem.split(' ')[1]}')
print(f'Cidade: {mensagem[mensagem.index('São'):mensagem.find('-')].strip()}')
if mensagem.find('pendente') != -1:
    print(f'Pendente encontrado: {True}')
else:
    print(f'Pendente encontrado: {False}')
print(20 * '-=')   


# ============================================================
# EXERCÍCIO 04 — PADRONIZAÇÃO DE REGISTROS
# NÍVEL: INTERMEDIÁRIO
# ============================================================
#
# Um sistema exportou um registro com espaços
# desnecessários e diferenças entre letras maiúsculas
# e minúsculas.
#
# TAREFAS:
# 1. Remova os espaços desnecessários.
# 2. Extraia o número do pedido.
# 3. Extraia o status.
# 4. Padronize o status para letras minúsculas.
# 5. Apresente o registro no formato solicitado.
#
# RESULTADO ESPERADO:
#
# PEDIDO: 1258 | STATUS: pendente
#
# REGRAS:
# - Não escreva manualmente o número ou o status.
# - Utilize métodos de string.
#
# ============================================================

registro = "  pedido: 1258 | status: PENDENTE  "



# ESCREVA SUA SOLUÇÃO ABAIXO:
# Vou criar uma nova variável mesmo que seja desnecessária
registro_tratado = registro.strip()
# print(f'Número do Pedido: {registro_tratado[registro_tratado.index('1'):registro_tratado.find('8')+1]}') # Propositalmente alterei entre index e find 
print(f'Número do Pedido: {registro_tratado.split(' ')[1]}')
print(f'Status: {registro_tratado[registro_tratado.rindex('P'):].lower()}')
print(f'PEDIDO:  {registro_tratado.split(' ')[1]} | STATUS: {registro_tratado[registro_tratado.rindex('P'):].lower()}')

# ============================================================
# EXERCÍCIO 05 — INVESTIGAÇÃO DE COMPORTAMENTO
# NÍVEL: INTERMEDIÁRIO
# ============================================================
#
# Analise o código abaixo ANTES de executá-lo.
#
# TAREFAS:
# 1. Preveja o resultado do primeiro print().
# 2. Preveja o que acontecerá no segundo print().
# 3. Explique a diferença entre find() e index().
# 4. Explique quando essa diferença pode ser importante
#    ao processar dados recebidos de sistemas externos.
#
# REGRAS:
# - Primeiro escreva suas previsões em comentários.
# - Depois execute o código.
# - Compare o resultado com suas previsões.
#
# ============================================================

texto = "engenharia de dados"

# SUAS PREVISÕES:
#
# 1.
# Não vai retornar pois a palavra python não existe em texto
# 2.
# A mesma situação
# 3.
# Se achar o texto não tem diferença, mas quando não acha o find retonar -1 enquando index da value error
# 4.
# O value error é interessante quando queremos que um erro suba e mostre , mas nem sempre queremos tratar essas excessões e usamos o find

print(texto.find("Python"))
# print(texto.index("Python"))




# ============================================================
# EXERCÍCIO 06 — MINI-DESAFIO DE ENGENHARIA DE DADOS
# NÍVEL: DESAFIADOR
# ============================================================
#
# Uma transportadora exportou os dados de uma entrega
# em uma única linha de texto.
#
# TAREFAS:
# 1. Remova os espaços desnecessários.
# 2. Separe os campos utilizando o delimitador ";".
# 3. Extraia a data.
# 4. Extraia o identificador do pedido.
# 5. Padronize o nome do cliente em maiúsculas.
# 6. Padronize o status em minúsculas.
# 7. Converta o valor para float.
# 8. Apresente os resultados utilizando f-strings.
#
# RESULTADO ESPERADO:
#
# Data: 2026-10-20
# Pedido: PED-1058
# Cliente: JOÃO SILVA
# Status: entregue
# Valor: R$ 350.75
#
# REGRAS:
# - Não escreva manualmente os valores extraídos.
# - Utilize os conteúdos estudados até agora.
# - Não utilize bibliotecas externas.
#
# ============================================================

linha = "  2026-10-20;PED-1058;joão silva;ENTREGUE;350.75  "


# ESCREVA SUA SOLUÇÃO ABAIXO:
# Por escolha minha vou colocar em variáveis
linha_tratada = linha.strip().split(';')
data = linha_tratada[0]
pedido = str(linha_tratada[1])
cliente = str(linha_tratada[2])
status = str(linha_tratada[3])
valor = float(linha_tratada[4])
print(f'''
Data: {data}
Pedido: {pedido}
Cliente: {cliente.upper()}
Status: {status.lower()}
Valor: R$ {valor}''')