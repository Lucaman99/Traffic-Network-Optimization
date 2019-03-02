#Graph --> Nodes, Edges

#Players --> Start, end, route

#Creates a graph object

class Graph:
    def __init__(self, node_set, edges_set, weight):
        self.node_set = node_set
        self.edges_set = edges_set
        self.weight = weight
        
#Connects nodes with an edge
    def connect_nodes(self, edge, weight):
        if (edge not in self.edges_set):
            self.edges_set.append(edge)
            self.weight.append(weight)
            
#Adds a node to the graph
    def add_nodes(self, node):
        if (node not in self.node_set):
            self.node_set.append(node)

#Removes nodes from the graph. If a node is removed, all edges connected to that node are removed as well

    def remove_nodes(self, node):
        if (node in self.node_set):
            del self.node_set[self.node_set.index(node)]
            for i in self.edges_set:
                if (node in i):
                    del self.edges_set[self.edges_set.index(i)]
                    
#Disconnects nodes, thereby removing an edge
    def disconnect_nodes(self, edge, weight):
        if (edge in self.edges_set):
            del self.edges_set[self.edges_set.index(edge)]
            del self.weight[self.edges_set.index(edge)]

#Checks if the graph is completely connected (no disjoint sections of the graph)
    def check_connectivity(self, weight):
        counter = 0
        branching_values = [self.node_set[0]]
        for value in self.edges_set:
            if (value[0] in branching_values and value[1] not in branching_values):
                branching_values.append(value[1])
        if (len(branching_values) == len(self.node_set)):
            return True
        else:
            return False

'''
Algorithm to check connectivity:
1. Choose an arbitrary node x of the graph G as the starting pointself.
2. Determine the set A of all nodes which can be reached from x.
3. If A is equal to the set of all nodes of G, the graph is connected; otherwise it is disconnected.
'''

#Defines a player object

class Player:

    def __init__(self, route, graph): #Route includes a start point and an end point, therefore there is no need to define these
        self.route = route
        self.graph = [graph.node_set, graph.edges_set]

    #Changes the route of a player

    def change_route(self, route):
        self.change_route = route

    #Checks if the route that the player is taking is a subgraph of the larger, previously defined graph network

    def check_legal_route(self):
        for i in range(0, len(self.route)-1):
            if ([self.route[i], self.route[i+1]] in self.graph[1]):
                return True
            else:
                return False
