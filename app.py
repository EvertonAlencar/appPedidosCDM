from flask import Flask, request, jsonify
import assembleOrder
import printOrder


app = Flask(__name__)

@app.route('/getData', methods=['GET'])
def mostrarPedidos():
    return jsonify(assembleOrder.orders)


@app.route('/sendOrder',methods=['PUT'])
def receiveOrder():
    order = assembleOrder.orders[0]
    receivedOrder = request.get_json()
    order.update(receivedOrder)
    printOrder.printOrder(assembleOrder.assembleOrder(order['apartamentNumber'],order['tableNumber'],order['body'],order['observation'],order['clothesDescription']))
    return jsonify(assembleOrder.orders)

app.run('0.0.0.0', debug=True)