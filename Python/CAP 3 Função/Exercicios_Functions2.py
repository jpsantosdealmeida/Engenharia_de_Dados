# ============================================================
# CAPÍTULO 2 — FUNÇÕES EM PYTHON
# TEMA: FUNÇÕES ANINHADAS E DECORATORS
# ============================================================
#
# OBJETIVO:
# Entender como uma função pode:
# - Ser armazenada em uma variável.
# - Ser passada como argumento para outra função.
# - Ser retornada por outra função.
# - Ser definida dentro de outra função.
# - Ser utilizada com decorators.
#
# REGRA:
# Não avance para o próximo exercício sem entender o anterior.
# Não precisa utilizar conceitos que ainda não estudamos.
#
# ============================================================
# EXERCÍCIO 01 — FUNÇÃO COMO VARIÁVEL
# DIFICULDADE: FÁCIL
# ============================================================
#
# 1. Crie uma função chamada saudacao().
# 2. Dentro dela, imprima "Bem-vindo ao Python!".
# 3. Crie uma variável chamada mensagem.
# 4. Atribua a função saudacao à variável mensagem,
#    sem executar a função nesse momento.
# 5. Execute a função utilizando a variável mensagem.
#
# PERGUNTAS:
# - Qual a diferença entre mensagem = saudacao e mensagem = saudacao()?
# mensagem = saudacao - Obj mensagem faz referencia a def saudacao , para executar preciso chamar mensagem()
# e mensagem = saudacao() - Já estou executando a função ...
# - O que acontece quando utilizamos mensagem()?
# Executada a impressão 

def saudacao():
    print("Bem-vindo ao Python!")

mensagem = saudacao


# ============================================================
# EXERCÍCIO 02 — FUNÇÃO COMO ARGUMENTO
# DIFICULDADE: FÁCIL
# ============================================================
#
# 1. Crie uma função chamada mostrar_mensagem().
# 2. Ela deverá imprimir "Processamento concluído!".
#
# 3. Crie outra função chamada executar_funcao(funcao).
# 4. Essa função deverá:
#    - Imprimir "Iniciando execução".
#    - Executar a função recebida como argumento.
#    - Imprimir "Execução finalizada".
#
# 5. Passe mostrar_mensagem como argumento de executar_funcao.
#
# RESULTADO ESPERADO:
#
# Iniciando execução
# Processamento concluído!
# Execução finalizada
#
# PERGUNTA:
# - Por que passamos mostrar_mensagem sem parênteses?
# Pq a execução é feita em executar funcao na linha 74 funcao()
# def mostrar_mensagem():
#     print("Processamento concluído!")


# def executar_funcao(funcao):
#     print("Iniciando execução")
#     funcao()
#     print("Execução finalizada")

# executar_funcao(mostrar_mensagem)

# ============================================================
# EXERCÍCIO 03 — RETORNANDO UMA FUNÇÃO
# DIFICULDADE: INTERMEDIÁRIA
# ============================================================
#
# 1. Crie uma função chamada selecionar_operacao(numero).
#
# 2. Dentro dela, crie duas funções:
#
#    - somar():
#      Deverá imprimir o resultado de 10 + 5.
#
#    - multiplicar():
#      Deverá imprimir o resultado de 10 * 5.
#
# 3. Na função selecionar_operacao:
#
#    - Se numero == 1, retorne a função somar.
#    - Se numero == 2, retorne a função multiplicar.
#
# 4. Armazene o retorno de selecionar_operacao(1)
#    em uma variável chamada resultado.
#
# 5. Execute resultado().
#
# 6. Repita o processo utilizando selecionar_operacao(2).
#
# RESULTADOS ESPERADOS:
#
# Operação 1: 15
# Operação 2: 50
#
# PERGUNTAS:
# - O que está armazenado em resultado?
# - Por que retornar somar é diferente de retornar somar()?
def selecionar_operacao(numero):
    if numero == 1:
        def somar():
            print(10+5)


# def selecionar_operacao(numero):
#     if numero == 1:
#         def somar():
#             return 10 + 5
        
#     elif numero == 2:
#         def multiplicar():
#             return 10 * 5

#     else:
#         print(f'Número {numero} inválido.')




# ============================================================
# EXERCÍCIO 04 — CRIANDO UM DECORATOR MANUALMENTE
# DIFICULDADE: INTERMEDIÁRIA
# ============================================================
#
# 1. Crie uma função chamada registrar_execucao(funcao).
#
# 2. Dentro dela, crie outra função chamada wrapper().
#
# 3. A função wrapper deverá:
#
#    - Imprimir "Iniciando processamento..."
#    - Executar a função recebida em registrar_execucao.
#    - Imprimir "Processamento finalizado!"
#
# 4. A função registrar_execucao deverá retornar wrapper,
#    sem executá-la.
#
# 5. Fora dessas funções, crie processar_dados().
#    Ela deverá imprimir "Processando registros...".
#
# 6. Faça a seguinte chamada:
#
#    resultado = registrar_execucao(processar_dados)
#
# 7. Execute resultado().
#
# RESULTADO ESPERADO:
#
# Iniciando processamento...
# Processando registros...
# Processamento finalizado!
#
# PERGUNTAS:
# - Qual função está armazenada em resultado?
# - Em que momento processar_dados é executada?
#
#
# ============================================================
# EXERCÍCIO 05 — UTILIZANDO @DECORATOR
# DIFICULDADE: INTERMEDIÁRIA
# ============================================================
#
# Agora vamos utilizar a sintaxe @.
#
# 1. Reaproveite a função registrar_execucao
#    criada no exercício anterior.
#
# 2. Crie uma função chamada importar_arquivo().
#    Ela deverá imprimir "Importando arquivo CSV...".
#
# 3. Aplique @registrar_execucao sobre importar_arquivo.
#
# 4. Execute importar_arquivo().
#
# RESULTADO ESPERADO:
#
# Iniciando processamento...
# Importando arquivo CSV...
# Processamento finalizado!
#
# PERGUNTAS:
# - Qual a diferença entre o exercício 04 e o 05?
# - O que o @registrar_execucao faz?
# - Por que importar_arquivo() também executa wrapper()?
#
#
# ============================================================
# EXERCÍCIO 06 — QUANDO O DECORATOR É EXECUTADO?
# DIFICULDADE: DESAFIO DE RACIOCÍNIO
# ============================================================
#
# Analise o código abaixo ANTES de executá-lo.
#
# def decorador(funcao):
#     print("A")
#
#     def wrapper():
#         print("B")
#         funcao()
#         print("C")
#
#     return wrapper
#
#
# @decorador
# def executar():
#     print("D")
#
#
# print("E")
# executar()
#
#
# DESAFIO:
# 1. Escreva qual será a ordem das letras no terminal.
# 2. Execute o código para conferir.
# 3. Explique por que a primeira letra aparece
#    antes da chamada executar().
# 4. Identifique quais mensagens são impressas
#    quando o decorator é aplicado e quais são
#    impressas quando wrapper() é executada.
#
#
# ============================================================
# CONCLUSÃO
# ============================================================
#
# Ao terminar, você deverá conseguir explicar:
#
# 1. A diferença entre funcao e funcao().
# 2. Como passar funções como argumentos.
# 3. Como retornar funções.
# 4. Como funcionam funções aninhadas.
# 5. O papel da função wrapper.
# 6. O significado da sintaxe @decorator.
#
# Não se preocupe com decorators que recebem argumentos,
# *args, **kwargs ou functools.wraps por enquanto.
#
# Primeiro vamos dominar a estrutura básica.
# ============================================================