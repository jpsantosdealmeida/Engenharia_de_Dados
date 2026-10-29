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


    

def processamento():
# O programa deverá identificar registros inválidos, contar os pedidos válidos por status e calcular o valor total dos pedidos entregues.
    validos = 0
    entregues = 0 
    cancelados = 0 
    valor_total_entregues = 0 
    invalidos = 0
    index_invalidos = []


    for x in range(0,len(valores_validos)):
        if valores_validos[x] == False:
            # print(f'Erro no pedido no index: {x}')
            invalidos += 1
            index_invalidos.append(x)

    # Vou usar while para treinar ele também
    c = 0
    
    
    while c < len(index_invalidos):
        valores_validos.pop() # Removendo os ultimos
        c += 1
        print(valores_validos)

    
    
        
processamento()




