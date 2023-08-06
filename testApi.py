import requests
i = 0
url = 'http://10.0.0.100:5000/sendOrder'
apartament = input('Digite o numero do apartamento: ')
table = input('digite o numero da mesa: ')
body = input('digite os pedidos separados por virgula: ')
observation = input('digite uma observação: ')


sendOrder = {
    'id' : 0,
    'apartamentNumber' : apartament,
    'tableNumber' : table,
    'body': body.replace(',','\n'),
    'observation' : observation
}

response = requests.put(url,json=sendOrder)