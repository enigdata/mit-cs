### Nodes and Edges 
class Node(object):
    def __init__(self, name):
        self.name = name 

    def getName(self):
        return self.name 

    def __str__(self):
        return self.name 

class Edge(object):
    def __init__(self, src, dest):
        '''
        src and dest are nodes
        '''
        self.src = src 
        self.dest = dest  
    
    def getSource(self):
        return self.src 

    def getDestination(self):
        return self.dest  

    def __str__(self):
        return self.src.getName() + '->' self.dest.getName() 

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight = 1.0):
        self.src = src  
        self.dest = dest 
        self.weight = weight 

    def getWeight(self):
        return self.weight

    def __str__(self):
        return self.src.getName() + '->(' + str(self.weight) + ')'\
            + self.dest.getName() 

#Implementation of Digraph and Graph
class Digraph(object):
    #nodes is a list of the nodes in the graph
    #edges is a dict mapping each node to a list of its children

    def __init__(self):
        self.nodes = []
        self.edges = {}

    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.node.append(node)
            self.edges[node] = [] 

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        '''
        get all the children of the node
        '''
        return self.edges[node]

    def hasNode(self, node):
        return node in self.nodes 

    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                    + dest.getName() + '\n'
        return result[:-1] 

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge):
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

##### Shortest Path problem 
# 
def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago', 'Denver', 'Phoenix', 'Los Angeles'):
        g.addNode(Node(name))

    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g 

### DFS: depth first search 
# avoid loops 

#one example implementation of DFS 
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'A'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() #keep track of visited nodes 

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

#back to our example
def DFS(graph, start, end, path = [], shortest = None, toPrint = False):
    path = path + [start]
    if toPrint:
        print('Current DFS path: ', path)

    if start == end:
        print('DFS path: ', path)

    for node in graph.childrenOf(start):
        if node not in path: #avoid cycles
            if shortest is None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint)
                if newPath is not None:
                    shortest = newPath 

            elif toPrint:
                print('Already visited ', node)
    return shortest


####BFS: breadth first search 
def BFS(graph, start, end, toPrint=False):
    initPath = [start]
    pathQueue = [initPath] # a list of paths; something to explore
    while len(pathQueue) > 0: #while I still get things to explore
        #get and remove oldest element in pathQueue
        tmpPath = pathQueue.pop(0)
        if toPrint:
            print('Current BFS path: ', path)
        lastNode = tmpPath[-1]
        if lastNode == end:
            return tmpPath

        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath = tmpPath + [nextNode]
                pathQueue.append(newPath)

    return None 


        


   