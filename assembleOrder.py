import datetime

orders = [
    {
        'id' : 0,
        'apartamentNumber' : '',
        'tableNumber' : '',
        'body' : '',
        'observation': ''
    }
]

def assembleOrder(apartamentNumber,tableNumber,bodyOrder,observation):
    getApartamentNumber = apartamentNumber
    getTableNumber = tableNumber
    getBodyOrder = bodyOrder
    getObservation = observation
    main = """
------------------------------------------------
Apartamento: {0}
Numero da mesa: {1}
Data: {2}
------------------------------------------------
Pedidos                                      qtd
{3}

observacao: {4}
------------------------------------------------





""".format(getApartamentNumber,getTableNumber,datetime.datetime.now().strftime('%d/%m/%y'),getBodyOrder,getObservation)
    header = bytes(main,'ISO-8859-1')
    
    return header
