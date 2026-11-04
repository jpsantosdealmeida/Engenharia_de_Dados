from datetime import datetime
from time import sleep

# ============================================================
# DESAFIO 07 — REFATORAÇÃO DE CÓDIGO
# PROJETO: LOGIDATA
# ============================================================
#
# CENÁRIO:
# Uma transportadora possui um programa que processa pedidos.
# O código funciona, mas concentra muitas responsabilidades.
#
# SUA MISSÃO:
# Refatorar o programa utilizando os conceitos estudados
# no capítulo de funções.
#
# REGRAS:
# 1. Não alterar os dados originais.
# 2. Manter os mesmos resultados.
# 3. Dividir responsabilidades entre funções.
# 4. Utilizar parâmetros e retornos adequadamente.
# 5. Evitar depender de variáveis globais.
# 6. Criar um decorator para registrar o início e o fim
#    do processamento.
# 7. Utilizar try/except para tratar valores inválidos.
#
# EXTRA (OPCIONAL):
# Medir o tempo de execução com datetime.
#
# ============================================================
# BASE DE DADOS
# ============================================================

pedidos = [
    "PED-001;ENTREGUE;350.00;São Paulo",
    "PED-002;PENDENTE;780.50;Campinas",
    "PED-003;ENTREGUE;120.00;Santos",
    "PED-004;CANCELADO;500.00;Sorocaba",
    "PED-005;ENTREGUE;abc;Jacareí",
    "PED-006;ENTREGUE;-100.00;Taubaté",
    "PED-007;PENDENTE;250.00;São Paulo",
    "PED-008;ENTREGUE;890.00;Campinas",
    "PED-009;DESCONHECIDO;300.00;Santos",
    "PED-010;ENTREGUE;450.00;São Paulo"
]

# ============================================================
# CÓDIGO LEGADO — NÃO ESTÁ REFATORADO
# ============================================================

print("=" * 45)
print("INICIANDO PROCESSAMENTO LOGÍSTICO")
print("=" * 45)

inicio = datetime.now()

entregues = 0
pendentes = 0
cancelados = 0

faturamento = 0

# ============================================================
# FUNÇÕES
# ============================================================

def validar_invalidos(tamanho = 0,codigo = '0',cidade = '0',status = 'entregue'):

    invalidos = 0
    if tamanho != 4:
        invalidos += 1

    if codigo == "" or cidade == "":
        invalidos += 1

    if status not in ["entregue", "pendente", "cancelado"]:
        invalidos += 1

    
        

    
        
    return invalidos


for pedido in pedidos:

    campos = pedido.split(";")

    # if len(campos) != 4:
    #     invalidos += 1
    #     continue

    codigo = campos[0].strip()
    status = campos[1].strip().lower()
    valor = campos[2].strip()
    cidade = campos[3].strip()


    validar_invalidos(tamanho= len(campos),cidade=cidade,codigo=codigo,status=status)


invalidos = validar_invalidos()
print(invalidos)

#     if codigo == "" or cidade == "":
#         invalidos += 1
#         continue

#     if status not in ["entregue", "pendente", "cancelado"]:
#         invalidos += 1
#         continue

#     try:
#         valor = float(valor)
#     except ValueError:
#         invalidos += 1
#         continue

#     if valor <= 0:
#         invalidos += 1
#         continue

#     if status == "entregue":
#         entregues += 1
#         faturamento += valor

#     elif status == "pendente":
#         pendentes += 1

#     elif status == "cancelado":
#         cancelados += 1

#     sleep(0.2)

# fim = datetime.now()
# print()
# print("=" * 45)
# print("RELATÓRIO FINAL")
# print("=" * 45)

# print(f"Pedidos entregues: {entregues}")
# print(f"Pedidos pendentes: {pendentes}")
# print(f"Pedidos cancelados: {cancelados}")
# print(f"Pedidos inválidos: {invalidos}")
# print(f"Faturamento: R$ {faturamento:.2f}")

# print("=" * 45)
# print(f"Tempo de execução: {fim - inicio}")
# print("=" * 45)