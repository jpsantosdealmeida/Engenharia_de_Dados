pedidos = [
 
    "PED-013;ENTREGUE;250.00;",
    "PED-014;ENTREGUE;250.00;   ",
    "PED-015;PENDENTE;100.00;Campinas;EXTRA",
    "PED-016;ENTREGUE;300.00;São Paulo"
]


cancelados = 0 
entregues = 0 
erros = 0
pendentes = 0
total = 0



for pedido in pedidos: 
    campo = pedido.split(';')
    id = campo[0].strip()

    # Verificando se tem cidade
    if len(campo) == 4 and campo[3].strip() != '':
        cidade = campo[3].strip()
        status = campo[1].strip().lower()
        valor = campo[2].strip()
    else:
        print(f'Pedido: {id} sem cidade ,corrigir.')
        erros += 1
        continue

    # Verificando se status está entre entregue,cancelado e pendente
    if status not in ('entregue','cancelado','pendente'):
        print(f'Pedido: {id} com status: {status},corrigir.')
        erros += 1
        continue
    # else:
    #     if status == 'cancelado':
    #         cancelados += 1 
    #     elif status == 'pendente':
    #         pendentes += 1
    #     else:
    #         erros += 1
            
    
    # Verificando todos os valores estão sendo convertidos para float
    try:
        valor = float(valor)
        if valor > 0:
            if status == 'entregue':
                total += valor
                entregues += 1
        # Para valores < 0 e negativos 
        else:
            print(f'Pedido: {id} com valor incorreto: {valor},corrigir.')
            erros += 1
            continue
    except ValueError:
        print(f'Pedido: {id} com valor incorreto: {valor},corrigir.')
        erros += 1
        continue

    # contagem
    if status == 'cancelado':
        cancelados += 1 
    elif status == 'pendente':
        pendentes += 1
      

    print(f'''
            Pedido: {id}
            Status: {status}
            Valor: {valor}
            Cidade: {cidade}
------------------------------''')
if entregues > 0:
    ticketmedio = total / entregues
else:
    ticketmedio = 0
print(f'Ticket Médio: {round(ticketmedio,2)}')    
print(f'Erros: {erros}')
print(f'Cancelados: {cancelados}')
print(f'Entregues: {entregues}')
print(f'Valor Total dos Entregues: {total}')
