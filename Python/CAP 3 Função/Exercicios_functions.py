# ============================================================
# EXERCÍCIO 01 — CALCULADORA DE FRETE
# ============================================================
# Objetivo:
# Criar uma função que receba o peso e a distância de uma
# entrega, calcule o valor do frete e retorne o resultado.
#
# Fórmula:
# Frete = (peso * 2.5) + (distancia * 0.75)
# ============================================================

def calcular_frete(peso, distancia):
    valor_frete = (peso * 2.5) + (distancia * 0.75)
    return valor_frete

frete1 = calcular_frete(10, 100)
frete2 = calcular_frete(25, 200)
frete3 = calcular_frete(50, 150)


# ============================================================
# EXERCÍCIO 02 — CLASSIFICADOR DE PEDIDOS
# ============================================================
# Objetivo:
# Criar uma função que receba o status de um pedido,
# remova espaços desnecessários, padronize o texto e
# retorne sua classificação.
#
# Regras:
# entregue  -> Finalizado
# pendente  -> Em andamento
# cancelado -> Cancelado
# outros    -> Status inválido
# ============================================================

def classificar_pedido(status):
    status = status.strip().lower()

    if status == 'entregue':
        return 'Finalizado'
    elif status == 'pendente':
        return 'Em andamento'
    elif status == 'cancelado':
        return 'Cancelado'
    else:
        return 'Status inválido'


classificacao = classificar_pedido('    cancelado   ')


# ============================================================
# EXERCÍCIO 03 — VALIDADOR DE VALORES
# ============================================================
# Objetivo:
# Criar uma função que receba um valor, tente convertê-lo
# para float e verifique se é maior que zero.
#
# Retornos:
# True  -> Valor válido e positivo
# False -> Valor inválido, zero ou negativo
#
# Conceitos:
# Funções, return, condicionais e tratamento de exceções.
# ============================================================

def validar_valor(valor):

    try:
        valor = float(valor)
        if type(valor) == float and valor > 0:
            return True
        else:
            return False
    except:
        return False


valores = ["350.00", "0", "-150.00", "abc", "890.50"]
resultado = validar_valor("-150.00")


# ============================================================
# EXERCÍCIO 04 — REGISTRO DE ENTREGAS
# ============================================================
# Objetivo:
# Criar uma função que receba o identificador do pedido,
# a cidade e o status da entrega.
#
# O parâmetro status deve possuir o valor padrão 'pendente'.
# A função deve retornar uma mensagem com os dados recebidos.
#
# Conceitos:
# Argumentos posicionais, argumentos nomeados,
# parâmetros com valor padrão e return.
# ============================================================

def registrar_entrega(pedido, cidade, status='pendente'):
    return f'O pedido {pedido} passou pela cidade {cidade} e seu status é {status}'


re1 = registrar_entrega(pedido='PED-001', cidade='Campinas')
re2 = registrar_entrega(pedido="PED-001", cidade='Campinas', status='Pendente')
re3 = registrar_entrega('PED-001', 'Jacareí', 'entregue')

print(re1)
print(re2)
print(re3)


# ============================================================
# EXERCÍCIO 05 — SOMA DE FRETES COM *ARGS
# ============================================================
# Objetivo:
# Criar uma função que receba uma quantidade variável
# de valores de frete e retorne a soma de todos eles.
#
# A função também deve funcionar quando nenhum argumento
# for informado.
#
# Conceitos:
# *args, argumentos posicionais variáveis,
# tuplas, função sum() e return.
# ============================================================

def somar_fretes(*valor_frete):
    vl_frete = sum(valor_frete)
    return vl_frete


sf1 = somar_fretes(100, 200, 50)
sf2 = somar_fretes(75, 125)
sf3 = somar_fretes()

print(sf1)
print(sf2)
print(sf3)