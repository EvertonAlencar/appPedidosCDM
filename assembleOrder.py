import datetime
from time import sleep

orders = [
    {
        'id' : 0,
        'apartamentNumber' : '',
        'tableNumber' : '',
        'body' : '',
        'observation': '',
        'clothesDescription': ''
    }
]

def assembleOrder(apartamentNumber,tableNumber,bodyOrder,observation,clothesDescription):
    getApartamentNumber = apartamentNumber
    getTableNumber = tableNumber
    getBodyOrder = bodyOrder
    getObservation = observation
    getClothesDescription = clothesDescription
    main = """
------------------------------------------------
Apartamento: {0}
Numero da mesa: {1}
Data: {2}
------------------------------------------------
Pedidos
{3}

Observacao: {4}
Vestimentas: {5}
------------------------------------------------





""".format(getApartamentNumber,getTableNumber,datetime.datetime.now().strftime('%d/%m/%y'),getBodyOrder,getObservation,getClothesDescription)
    header = bytes(main,'utf-8')
    return  header
