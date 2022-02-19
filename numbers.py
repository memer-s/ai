from random import seed
from random import random as randomNum
import pprint

seed(1)

# node = {weights: [], value: 0}

def random():
    if randomNum() > 0.5:
        return -randomNum()
    return randomNum()


def initNetwork(n_inputs, n_hidden_layers, n_hidden_nodes, n_outputs):
    network = { 'layers': [] }
    input_layer = {'layer': []}

    for _ in range(n_inputs):
        input_layer['layer'].append({'value': 0.98})
    network['layers'].append(input_layer)

    for _ in range(n_hidden_layers):
        hidden_layer = {'layer': []}

        for __ in range(n_hidden_nodes):
            node = {'weights': [], 'value': 0}

            for ___ in range(len(network['layers'][-1]['layer'])):
                node['weights'].append(random())
            
            hidden_layer['layer'].append(node)

        network['layers'].append(hidden_layer)
    
    outputs = {'layer': []}

    for _ in range(n_outputs):
        node = {'weights': [], 'value': 0}
        for __ in range(len(network['layers'][-1]['layer'])):
            node['weights'].append(random())
        outputs['layer'].append(node)

    network['layers'].append(outputs)

    return network


def calculate_sum(network):

    for i in range(len(network['layers'])-1):
        for j in range(len(network['layers'][i+1]['layer'])):
            sum = 0
            for k in range(len(network['layers'][i]['layer'])):
                sum += network['layers'][i+1]['layer'][j]['weights'][k] * network['layers'][i]['layer'][k]['value']
            network['layers'][i+1]['layer'][j]['value'] = sum

    return network
    
def get_output(network):
    value = []
    for i in range(len(network['layers'][-1]['layer'])):
        value.append(network['layers'][-1]['layer'][i]['value'])

    return value

def main():
    print("Author: @devMimer / Github: memer-s")
    net = initNetwork(2, 2, 4, 100)
    print(net)
    print("-----")
    net = calculate_sum(net)
    print(net)
    print(get_output(net))

if __name__ == "__main__":
    main()
