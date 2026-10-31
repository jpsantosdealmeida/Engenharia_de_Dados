# ============================================================
# Exercício no capítulo 2 - LogiData V2 ( com funções )
# ============================================================
# Sua tarefa é construir um programa que utilize pelo menos três funções, cada uma com uma responsabilidade:
# - Uma função para separar e interpretar os campos do pedido.
# - Uma função para validar o valor.
# - Uma função para processar os registros e calcular os indicadores.
# O programa deverá identificar registros inválidos, contar os pedidos válidos por status e calcular o valor total dos pedidos entregues.

# Por enquanto, pode continuar usando listas, laços e condicionais normalmente. Não precisa antecipar conteúdos de coleções avançadas ou orientação a objetos
# ============================================================
pedidos = [
    "PED-001;ENTREGUE;350.00",
    "PED-002;PENDENTE;780.50",
    "PED-003;ENTREGUE;120.00",
    "PED-004;CANCELADO;500.00",
    "PED-005;ENTREGUE;abc",
    "PED-006;ENTREGUE;-100.00"
]

def separador(lista):
    lista_pedidos= []
    for pedido in lista:
        lista_pedidos.append(pedido.split(';'))
    return lista_pedidos

lista_tratada = separador(pedidos)


def validador_valores(lista):
    lista_valores_validos = []
    for valor in lista:
        try:
            v = float(valor[2])
            if v > 0:
                lista_valores_validos.append(True)
            else:
                lista_valores_validos.append(False)
                
        except:
            lista_valores_validos.append(False)
            continue
    return lista_valores_validos

valores_validos = validador_valores(lista_tratada)


    

def processamento(lista_tratada):
    entregues = 0 
    cancelados = 0 
    pendentes = 0
    valor_total_entregues = 0 
    invalidos = 0
    desconhecidos = 0
    index_invalidos = []


    for x in range(0,len(valores_validos)):
        if valores_validos[x] == False:
            # print(f'Erro no pedido no index: {x}')
            invalidos += 1
            index_invalidos.append(x)

    c = 0
    while c < len(lista_tratada):
        if c in (index_invalidos):
            c += 1
            continue
            
        else:
            status = lista_tratada[c][1].lower()
            if status == 'entregue':
                valor_total_entregues += float(lista_tratada[c][2])
                entregues += 1
                
            elif status == 'pendente':
                pendentes += 1
            elif status == 'cancelado':
                cancelados += 1
            else:
                desconhecidos += 1
            

        c += 1
    
    print("\n" + "="*40)
    print("       RELATÓRIO DE PROCESSAMENTO       ")
    print("="*40)
    print(f" Registros Inválidos : {invalidos}")
    print("-"*40)
    print(f"  └─ Entregues       : {entregues}")
    print(f"  └─ Pendentes       : {pendentes}")
    print(f"  └─ Cancelados      : {cancelados}")
    print(f"  └─ Desconhecidos   : {desconhecidos}")
    print("-"*40)
    print(f" Faturamento Entregue: R$ {valor_total_entregues:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    print("="*40 + "\n")
         
processamento(lista_tratada)


