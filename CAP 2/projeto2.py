pedidos = [
    "PED-001;ENTREGUE;350.00;São Paulo",
    "PED-002;PENDENTE;780.50;Campinas",
    "PED-003;entregue;120.00;Santos",
    "PED-004;CANCELADO;500.00;Sorocaba",
    "PED-005;PENDENTE;250.00;São José dos Campos",
    "PED-006; ENTREGUE ; 890.00 ; Taubaté ",
    "PED-007;ENTREGUE;0;Jacareí",
    "PED-008;PENDENTE;-150.00;Guarulhos",
    "PED-009;DESCONHECIDO;300.00;Osasco",
    "PED-010;ENTREGUE;450.00;São Paulo",
    "PED-011;PENDENTE;620.00",
    "PED-012;ENTREGUE;abc;Campinas"
]

cancelados = 0 
entregues = 0 
erros = 0
pendentes = 0
total = 0



for pedido in pedidos: 
    id = pedido.split(';')[0].strip()
    status = pedido.split(';')[1].strip().lower()
    valor = pedido.split(';')[2].strip()

   
    
    # Verificando se tem cidade
    if len(pedido.split(';')) == 4:
        cidade = pedido.split(';')[3].strip()
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
            continue
    except :
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

ticketmedio = total / entregues
print(round(ticketmedio,2))    
print(erros)
print(cancelados)
print(entregues)
print(total)