# Desafio 01 — Contagem com condições
# Utilizando for e range(), percorra os números de 1 até 100.

# O programa deve identificar quantos números são pares, quantos são ímpares e apresentar as duas quantidades ao final.

par = 0
impar = 0


for numero in range (1,101):
    if numero % 2 == 0: #par
        par += 1
    else:
        impar += 1
print(f'Pares: {par}\nImpares: {impar}')
# Desafio 02 — Controle de tentativas
# Um sistema solicita uma senha ao usuário.

# A senha correta é "python123".

# O usuário poderá realizar no máximo três tentativas. Se acertar, apresente "ACESSO AUTORIZADO". Se errar as três, apresente "ACESSO BLOQUEADO".
# senha = ''
# tentativa = 0
# while tentativa < 3:
#     senha = input('Insira a senha: ')
#     tentativa += 1
#     if senha == "python123":
#         print("ACESSO AUTORIZADO")
#         break
#     if senha != "python123" and tentativa == 3:
#         print("ACESSO BLOQUEADO")

# Utilize while e estruturas condicionais.
# Desafio 03 — Análise de pedidos
# Considere:
pedidos = [    "PED-101;ENTREGUE;350",    "PED-102;PENDENTE;780",    "PED-103;ENTREGUE;120",    "PED-104;CANCELADO;500",    "PED-105;PENDENTE;250"]

# Percorra os registros com for e utilize split() para separar os campos.
# Ao final, apresente a quantidade de pedidos entregues, pendentes e cancelados, além da soma dos valores dos pedidos entregues.
entregues = 0
pendentes = 0
cancelados = 0
soma = 0
contador = 0

while contador < len(pedidos):
    status = pedidos[contador].split(';')[1].strip().lower()
    if pedidos[contador].split(';')[1].strip().lower() == 'entregue':
        entregues += 1
        soma += float(pedidos[contador].split(';')[2])
    elif pedidos[contador].split(';')[1].strip().lower() == 'pendente':
        pendentes += 1
    else:
        cancelados += 1
    contador += 1
print(f'Entregues: {entregues} | Valor: {soma}')
print(f'Pendentes: {pendentes}')
print(f'Cancelados: {cancelados}')
