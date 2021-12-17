from networkx.generators.random_graphs import erdos_renyi_graph

import networkx as nx
import matplotlib.pyplot as plt


def generateGraph():
    # number of nodes
    n = 10
    # probability of edge creation
    p = 0.5
    g = erdos_renyi_graph(n, p)
    print(g.nodes)
    print(g.edges)
    
    # Visualise the graphs, Uncomment the following 2 lines if you would like to see the graphs
    # nx.draw(g,with_labels=True)
    # plt.show()

    # Creation of nodes
    nodes = g.nodes
    # Creation of edges
    edges = g.edges

    check = []
    missing_num = False

    # Check whether the graph is connected.
    # Loop through the list of tuples containing connected nodes and check if the node appears at least once
    for eachnode in nodes:
        counter = 0
        for everyedge in edges:
            if eachnode in everyedge:
                counter += 1
            
        if counter == 0:
            missing_num = True

    if missing_num:
        print("The generated graph is disconnected")
    else:
        print("The generated graph is connected")
        check.append(0)

    lst = []
    for node in nodes:
        for edge in edges:
            if node in edge:
                lst.append(node)
   
    # Check if the graph contains a Euler circuit by checking the degree of each node
    test = False
    for n in nodes:
        if n in lst:
            var = lst.count(n)  # var = 1
            # Check if the node has an even degree
            if var % 2 != 0:
                test = True
    if test:
        print("The graph is not a Euler Circuit")
    else:
        print("The graph is a Euler Circuit")
        check.append(1)


    #print(check)
    return check


rounds = int(input("How many graphs would you like to be generate? "))
# Converting the number inserted by the user to a float
rounds = float(rounds)
# Keep track of the number of requirements passed
requirements = 0.0

for i in range(int(rounds)):
    # Loop to run the program depending of the number inputted by the user
    result=generateGraph()
    
    if len(result) == 2:
        requirements+=1

probability = requirements/float(rounds)

# bayes = prob/float(connected_count)

# print(prob)

print("The probability is: ", probability)