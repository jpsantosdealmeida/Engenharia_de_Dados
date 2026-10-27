
# ============================================================
# PYTHON — DIA 03
# REVISÃO: BOOLEANOS, OPERADORES LÓGICOS E CONDICIONAIS
# ============================================================
#
# Conteúdos:
# - bool(), int(), float(), str()
# - Operadores de comparação
# - and, or, not
# - if, elif, else
# - input() e f-strings
# - Métodos de strings
#
# REGRAS:
# 1. Não escreva manualmente os resultados.
# 2. Teste diferentes valores.
# 3. Não utilize bibliotecas externas.
# 4. Não precisa utilizar funções ou laços.
# 5. Resolva usando os conceitos estudados.
#
# ============================================================


# ============================================================
# EXERCÍCIO 01 — ANÁLISE DE EXPRESSÕES BOOLEANAS
# NÍVEL: FÁCIL / INTERMEDIÁRIO
# ============================================================
#
# Antes de executar, tente prever o resultado de cada
# expressão.
#
# TAREFAS:
# 1. Avalie cada expressão.
# 2. Armazene cada resultado em uma variável.
# 3. Imprima os resultados.
# 4. Escreva em comentários por que cada expressão
#    retorna aquele resultado.
#
# EXPRESSÕES:
#
# A) idade >= 18 and possui_cnh
# B) saldo > 1000 or limite > 500
# C) not ativo
# D) idade < 18 or not possui_cnh
# E) bool("False")
# F) bool(0)
#
# DESAFIO:
# Explique por que bool("False") não é igual a False.
#
# ============================================================

idade = 20
possui_cnh = False
saldo = 800
limite = 600
ativo = True


# # SUA SOLUÇÃO:

# # A) idade >= 18 and possui_cnh
# print(idade >= 18 and possui_cnh)
# #( Resultado: FALSE )
# # como tem que respeitar as 2 condições , no caso falta a cnh
# # B) saldo > 1000 or limite > 500
# print(saldo > 1000 or limite > 500) 
# # TRUE pois precisa respeitar umas das condições, o limite é maior que 500
# # C) not ativo
# # FALSE pois ativo tem que ser false e ele é true
# print(not ativo)
# # D) idade < 18 or not possui_cnh
# print(idade < 18 or not possui_cnh)
# # vai dar true pois realmente não possui cnh , precisa respeitar 1 condição
# # E) bool("False")
# print(bool('False'))
# print(type(bool('False')))
# # True pois foi convertido para bool 
# # F) bool(0)
# print(bool(0))
# bool 0 igual a false por seria a representação do binário no caso, false é 0 e > 0 é true

# a E e F ficou intgrante o pq do treu


# ============================================================
# EXERCÍCIO 02 — CLASSIFICAÇÃO DE NOTAS
# NÍVEL: INTERMEDIÁRIO
# ============================================================
#
# Um sistema precisa classificar o desempenho de um aluno.
#
# TAREFAS:
# 1. Solicite uma nota de 0 a 10.
# 2. Converta a entrada para float.
# 3. Verifique se a nota está dentro do intervalo válido.
# 4. Classifique o desempenho:
#
#    9 até 10      -> EXCELENTE
#    7 até < 9     -> APROVADO
#    5 até < 7     -> RECUPERAÇÃO
#    0 até < 5     -> REPROVADO
#
# 5. Se a nota estiver fora de 0 a 10, apresente
#    "NOTA INVÁLIDA".
#
# TESTES OBRIGATÓRIOS:
# - Nota 10
# - Nota 9
# - Nota 7
# - Nota 5
# - Nota 0
# - Nota -1
# - Nota 11
#
# ============================================================
# SUA SOLUÇÃO:
# print(30 * '=')
# nota = float(input('Insira a nota de 0 a 10: '))
# if nota > 10 or nota < 0:
#     print('Erro: Nota fora da faixa válida.')
# elif nota >= 9 and nota <= 10:
#     print('EXCELENTE')
# elif nota >= 7 and nota < 9:
#     print('APROVADO')
# elif nota >= 5 and nota < 7:
#     print('RECUPERAÇÃO')
# else:
#     print('REPROVADO')



# # ============================================================
# # EXERCÍCIO 03 — VALIDAÇÃO DE ACESSO
# # NÍVEL: INTERMEDIÁRIO
# # ============================================================
# #
# # Um sistema permite o acesso de funcionários.
# #
# # TAREFAS:
# # 1. Solicite o nome do funcionário.
# # 2. Solicite o departamento.
# # 3. Solicite se o funcionário está ativo (sim/não).
# # 4. Remova espaços e padronize as entradas.
# # 5. Conceda acesso somente quando:
# #
# #    - O funcionário estiver ativo.
# #    - O departamento for "TI" ou "DADOS".
# #    - O nome não estiver vazio.
# #
# # RESULTADOS POSSÍVEIS:
# #
# # "ACESSO AUTORIZADO"
# # "ACESSO NEGADO"
# #
# # TESTES:
# # - Funcionário ativo de TI.
# # - Funcionário ativo de Dados.
# # - Funcionário inativo de TI.
# # - Funcionário ativo de Financeiro.
# # - Nome vazio com departamento válido.
# #
# # DESAFIO:
# # Tente construir a condição usando and e or.
# # Observe a importância dos parênteses.
# #
# # ============================================================

# # SUA SOLUÇÃO:
# nome = input('Insira seu nome: ').strip().lower()
# dep = input('Insira seu departamento: ').strip().lower()
# ativo = input('Cadastro está ativo? (sim/nao): ').strip().lower()

# if (ativo == 'sim' and nome != '' ) and (dep == 'ti' or dep == 'dados'):
#     print('ACESSO AUTORIZADO')
# else:
#     print('ACESSO NEGADO')




# ============================================================
# EXERCÍCIO 04 — CLASSIFICAÇÃO DE ENTREGAS
# NÍVEL: INTERMEDIÁRIO
# ============================================================
#
# Uma transportadora recebe informações de entregas.
#
# TAREFAS:
# 1. Separe os campos utilizando split(";").
# 2. Padronize o status em letras minúsculas.
# 3. Converta os dias de atraso para int.
# 4. Classifique a entrega conforme as regras:
#
#    Status = entregue:
#       -> "FINALIZADA"
#
#    Status = pendente e atraso = 0:
#       -> "NO PRAZO"
#
#    Status = pendente e atraso entre 1 e 3:
#       -> "ATRASO LEVE"
#
#    Status = pendente e atraso maior que 3:
#       -> "ATRASO CRÍTICO"
#
#    Qualquer outro status:
#       -> "STATUS DESCONHECIDO"
#
# 5. Apresente o pedido e sua classificação.
#
# TESTES OBRIGATÓRIOS:
#
# "PED-101;PENDENTE;0"
# "PED-102;PENDENTE;2"
# "PED-103;PENDENTE;5"
# "PED-104;ENTREGUE;0"
# "PED-105;CANCELADO;0"
#
# Considere dias de atraso não negativos.
#
# ============================================================

# registro = "PED-102;PENDENTE;2"
# registro_tratado = registro.split(';')
# ped = registro_tratado[0]
# status = registro_tratado[1].lower()
# atraso = int(registro_tratado[2])
# if status == 'entregue':
#     print("FINALIZADA")

# elif status == 'pendente' and atraso == 0:
#     print("NO PRAZO")

# elif status == 'pendente' and atraso >= 1 and atraso <= 3:
#     print("ATRASO LEVE")

# elif status == 'pendente' and atraso >3:
#     print("ATRASO CRÍTICO")
# else:
#     print("STATUS DESCONHECIDO")





# ============================================================
# EXERCÍCIO 05 — ANÁLISE DE TRANSAÇÕES
# NÍVEL: DESAFIADOR
# ============================================================
#
# Um sistema financeiro precisa classificar transações
# recebidas de uma integração.
#
# TAREFAS:
# 1. Separe os dados pelo delimitador ";".
# 2. Converta o valor para float.
# 3. Padronize o tipo de transação em minúsculas.
# 4. Classifique conforme as regras:
#
#    Tipo = transferencia e valor > 5000:
#       -> "REVISÃO NECESSÁRIA"
#
#    Tipo = saque e valor > 2000:
#       -> "REVISÃO NECESSÁRIA"
#
#    Tipo = pagamento e valor <= 5000:
#       -> "APROVADA"
#
#    Tipo = transferencia e valor <= 5000:
#       -> "APROVADA"
#
#    Tipo = saque e valor <= 2000:
#       -> "APROVADA"
#
#    Qualquer outra combinação:
#       -> "NÃO CLASSIFICADA"
#
# 5. Apresente:
#    - Identificador
#    - Tipo
#    - Valor
#    - Classificação
#
# TESTES:
#
# "TX-001;TRANSFERENCIA;7500"
# "TX-002;SAQUE;2500"
# "TX-003;PAGAMENTO;150"
# "TX-004;TRANSFERENCIA;5000"
# "TX-005;SAQUE;2000"
# "TX-006;OUTRO;100"
#
# DESAFIO:
# Pense na ordem das condições.
# Verifique se uma condição pode impedir outra de
# ser executada.
#
# ============================================================

# transacao = "TX-001;TRANSFERENCIA;7500"
# num_transacao = transacao.split(';')[0]
# tipo = transacao.split(';')[1].lower()
# valor = float(transacao.split(';')[2])

# if  tipo == 'transferencia' and valor > 5000:
#     print(f'identificador = {num_transacao}\ntipo: {tipo}\nvalor: {valor}')
#     print("REVISÃO NECESSÁRIA")

# elif tipo == 'saque' and valor > 2000:
#     print(f'identificador = {num_transacao}\ntipo: {tipo}\nvalor: {valor}')
#     print("REVISÃO NECESSÁRIA")

# elif tipo == 'pagamento' and valor <= 5000:
#     print(f'identificador = {num_transacao}\ntipo: {tipo}\nvalor: {valor}')
#     print("APROVADA")

# elif tipo == 'transferencia' and valor <= 5000:
#     print(f'identificador = {num_transacao}\ntipo: {tipo}\nvalor: {valor}')
#     print("APROVADA")

# elif tipo == 'saque' and valor <= 2000:
#     print(f'identificador = {num_transacao}\ntipo: {tipo}\nvalor: {valor}')
#     print("APROVADA")
# else:
#     print(f'identificador = {num_transacao}\ntipo: {tipo}\nvalor: {valor}')
#     print("NÃO CLASSIFICADA")




# ============================================================
# EXERCÍCIO 06 — VALIDAÇÃO DE DADOS DE CLIENTES
# NÍVEL: DESAFIADOR
# ============================================================
#
# Uma empresa recebeu um cadastro de cliente de um
# sistema externo.
#
# TAREFAS:
# 1. Separe os campos utilizando ";".
# 2. Remova os espaços desnecessários.
# 3. Padronize o nome em maiúsculas.
# 4. Converta a idade para int.
# 5. Padronize o status em minúsculas.
# 6. Verifique se o cadastro atende às regras:
#
#    - Nome não pode estar vazio.
#    - Idade deve ser maior ou igual a 18.
#    - Status deve ser "ativo".
#    - E-mail deve conter "@" e ".".
#
# 7. Se TODAS as condições forem verdadeiras:
#       -> "CADASTRO VÁLIDO"
#
#    Caso contrário:
#       -> "CADASTRO INVÁLIDO"
#
# 8. Apresente os dados tratados e o resultado.
#
# TESTES OBRIGATÓRIOS:
#
# "João Silva;25;ATIVO;joao@email.com"
# "Maria;17;ATIVO;maria@email.com"
# "Carlos;30;INATIVO;carlos@email.com"
# ";22;ATIVO;teste@email.com"
# "Ana;28;ATIVO;anaemail.com"
#
# OBSERVAÇÃO:
# A verificação de e-mail é simplificada para fins
# de exercício. Não é uma validação completa.
#
# DESAFIO EXTRA:
# Em vez de verificar apenas o resultado final,
# apresente o motivo da invalidação.
#
# ============================================================

cadastro = "Maria;17;ATIVO;maria@email.com"


# SUA SOLUÇÃO:
# TAREFAS:
# 1. Separe os campos utilizando ";".
# 2. Remova os espaços desnecessários.
# 3. Padronize o nome em maiúsculas.
# 4. Converta a idade para int.
# 5. Padronize o status em minúsculas.
# 6. Verifique se o cadastro atende às regras:
#
nome = cadastro.split(';')[0].upper().strip()
idade = int(cadastro.split(';')[1].strip())
situacao = cadastro.split(';')[2].strip().lower()
email = cadastro.split(';')[3].strip()
ponto = email.find('.')
arroba = email.find('@')

#    - Nome não pode estar vazio.
#    - Idade deve ser maior ou igual a 18.
#    - Status deve ser "ativo".
#    - E-mail deve conter "@" e ".".

if nome != '' and idade >= 18 and situacao == 'ativo' and ponto != -1 and arroba != -1:
    print('CADASTRO VÁLIDO')
else:
    print('CADASTRO INVÁLIDO')


# ============================================================
# REFLEXÃO FINAL — DIA 03
# ============================================================
#
# 1. Qual exercício exigiu mais raciocínio?
#
# 2. Você utilizou and, or e not corretamente?
#
# 3. Em algum momento a ordem do if/elif/else
#    alterou o resultado?
#
# 4. Quais situações você não havia considerado
#    antes de testar o código?
#
# ============================================================
