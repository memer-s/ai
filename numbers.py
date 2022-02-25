from random import seed
from random import random as randomNum
from random import randint
import math
import pprint

seed(1)

# node = {weights: [], value: 0}

def random():
    if randomNum() > 0.5:
        return -randomNum()
    return randomNum()


def init_network(n_inputs, n_hidden_layers, n_hidden_nodes, n_outputs):
    network = { 'layers': [] }
    input_layer = {'layer': []}

    for _ in range(n_inputs):
        input_layer['layer'].append({'value': 0.7})
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

def squishification(val):
    return 1/(1+math.exp(-val))

def calculate_sum(network):
    for i in range(len(network['layers'])-1):
        for j in range(len(network['layers'][i+1]['layer'])):
            sum = 0
            for k in range(len(network['layers'][i]['layer'])):
                sum += (network['layers'][i+1]['layer'][j]['weights'][k] * network['layers'][i]['layer'][k]['value'] * 3)
            network['layers'][i+1]['layer'][j]['value'] = squishification(sum)

    return network

def set_input(network, inputs):
    for i in range(len(inputs)):
        network["layers"][0]["layer"][i]["value"] = inputs[i]
    return network
    
def get_output(network):
    value = []
    for i in range(len(network['layers'][-1]['layer'])):
        value.append(network['layers'][-1]['layer'][i]['value'])

    return value


def fitness(outputs, goals):
    deviation = 0

    for i in range(len(outputs)):
        deviation+=abs(outputs[i]-goals[i])

    return deviation

def crossover(net1, net2):
    child1 = net1
    child2 = net2

    children = [child1, child2]

    # weights: input -> first hidden layer
    for i in range(len(net1["layers"][1]["layer"])):
        for j in range(len(net1["layers"][1]["layer"][0]["weights"])):
            choice = math.floor(randomNum()*4.01)
            if(choice == 0):
                children[0]["layers"][1]["layer"][i]["weights"][j] = children[1]["layers"][1]["layer"][i]["weights"][j]
            elif(choice == 1):
                children[1]["layers"][1]["layer"][i]["weights"][j] = children[0]["layers"][1]["layer"][i]["weights"][j]
            elif(choice == 2):
                children[1]["layers"][1]["layer"][i]["weights"][j] = children[1]["layers"][1]["layer"][i]["weights"][j]
            elif(choice == 3):
                children[0]["layers"][1]["layer"][i]["weights"][j] = children[0]["layers"][1]["layer"][i]["weights"][j]
            else:
                if(randomNum()>0.5):
                    children[0]["layers"][1]["layer"][i]["weights"][j] = random()
                else:
                    children[1]["layers"][1]["layer"][i]["weights"][j] = random()


    # weights: n-hidden layer -> n+1-hidden layer
    for i in range(len(net1["layers"])-3):
        for j in range(len(net1["layers"][2]["layer"])):
            for k in range(len(net1["layers"][2]["layer"][0]["weights"])):
                choice = math.floor(randomNum()*4.01)
                if(choice == 0):
                    children[0]["layers"][i+2]["layer"][j]["weights"][k] = children[1]["layers"][i+2]["layer"][j]["weights"][k]
                elif(choice == 1):
                    children[1]["layers"][i+2]["layer"][j]["weights"][k] = children[0]["layers"][i+2]["layer"][j]["weights"][k]
                elif(choice == 2):
                    children[1]["layers"][i+2]["layer"][j]["weights"][k] = children[1]["layers"][i+2]["layer"][j]["weights"][k]
                elif(choice == 3):
                    children[0]["layers"][i+2]["layer"][j]["weights"][k] = children[0]["layers"][i+2]["layer"][j]["weights"][k]
                else:
                    if(randomNum()>0.5):
                        children[0]["layers"][i+2]["layer"][j]["weights"][k] = random()
                    else:
                        children[1]["layers"][i+2]["layer"][j]["weights"][k] = random()

    # weights: last hidden layer -> outputs
    for i in range(len(net1["layers"][-1]["layer"])):
        for j in range(len(net1["layers"][-1]["layer"][0]["weights"])):
            choice = math.floor(randomNum()*4.01)
            if(choice == 0):
                children[0]["layers"][-1]["layer"][i]["weights"][j] = children[1]["layers"][-1]["layer"][i]["weights"][j]
            elif(choice == 1):
                children[1]["layers"][-1]["layer"][i]["weights"][j] = children[0]["layers"][-1]["layer"][i]["weights"][j]
            elif(choice == 2):
                children[1]["layers"][-1]["layer"][i]["weights"][j] = children[1]["layers"][-1]["layer"][i]["weights"][j]
            elif(choice == 3):
                children[0]["layers"][-1]["layer"][i]["weights"][j] = children[0]["layers"][-1]["layer"][i]["weights"][j]
            else:
                if(randomNum()>0.5):
                    children[0]["layers"][-1]["layer"][i]["weights"][j] = random()
                else:
                    children[1]["layers"][-1]["layer"][i]["weights"][j] = random()

    return children


# takes in network with calculated sum
def selection(generation, goals):
    new_gene_pool = []
 
    for _ in range(len(generation)):
        net1 = generation[randint(0,len(generation)-1)]
        net2 = generation[randint(0,len(generation)-1)]

        # if net1 better than net2 kill net2
        if(abs(fitness(get_output(net1), goals)) < abs(fitness(get_output(net2), goals))):
            new_gene_pool.append(net1)
        else:
            new_gene_pool.append(net2)

    return new_gene_pool


def main():
    print("Author: @devMimer / Github: memer-s / https://memer.eu/")
    
    nr_generations = 100
    nr_nets = 100
    goals = (0,0,1,1,0.5,1)
    inputs = (0,0.4,0.2,0.4,0.3,0.7,1,0)

    networks = []
    
    for j in range(nr_generations):
        for i in range(nr_nets):
            networks.append(calculate_sum(set_input(init_network(8,10,10,6), inputs)))
        
        # selection includes mutation
        networks = selection(networks, goals)
        
        new_networks = []
        for i in range(int(nr_nets/2)):
            children = crossover(networks[(i*2)], networks[(i*2)+1])
            new_networks.append(children[0])
            new_networks.append(children[1])

        networks = new_networks
        if(j%25 == 0):
            print("fitness: "+str(fitness(get_output(networks[0]), goals)))

    print("after "+str(nr_generations)+" generations ----")
    print(networks[0])
    print("fitness: "+str(fitness(get_output(networks[0]), goals)))
    print("outputs: "+str(get_output(networks[0])))

def main_old():
    print("Author: @devMimer / Github: memer-s / https://memer.eu/")

    goals = (0,0,0,1,0,1)
    inputs = (0,0.4,0.2,0.4,0.3,0.7,1,0)
    net1 = init_network(8, 2, 4, 6)
    net2 = init_network(8, 2, 4, 6)
    net1 = set_input(net1, inputs)
    net2 = set_input(net2, inputs)
    print("-----")
    print(calculate_sum(net1))
    print("-----")
    print(calculate_sum(net2))
    print("-----")
    gen1 = crossover(net1, net2)
    print(calculate_sum(gen1[1]))
    print("outputs", get_output(net1))
    print("deviation", fitness(get_output(net1), goals))

if __name__ == "__main__":
    main()
