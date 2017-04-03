# Bellman Ford Algorithm for Shortest Path

import sys

# Function to create Nodes
class Node(object):
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacencyList = []
        # Distance from starting vertex/Node
        self.minDistance = sys.maxsize

# Function to create Edges
class Edge(object):
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex


# Bellman Ford Algorithm
class BellmanFord(object):
    # Initially set the Negative cycle flag to False
    HAS_CYCLE = False

    # Calculate the Shortest Path
    def calculateShortestPath(self, vertexList, edgeList, startVertex):
        startVertex.minDistance = 0
        for i in range(0,len(vertexList)-1):
            for edge in edgeList:
                u = edge.startVertex
                v = edge.targetVertex

                newDistance = u.minDistance + edge.weight
                if newDistance < v.minDistance:
                    v.minDistance = newDistance
                    v.predecessor = u

        for edge in edgeList:
            if self.hasCycle(edge):
                print('Negative cycle detected...')
                BellmanFord.HAS_CYCLE=True


    # Check if a negative cycle exists or not
    def hasCycle(self,edge):
        if (edge.startVertex.minDistance + edge.weight) < edge.targetVertex.minDistance:
            return True
        else:
            return False


    # Traceback and Print the Shortest Path
    def getShortestPath(self, targetVertex):
        if not BellmanFord.HAS_CYCLE:
            print('Shortest path exists with value: ', targetVertex.minDistance)
            node = targetVertex
            while node is not None:
                print('%s' % node.name)
                node = node.predecessor
        else:
            print('Negative cycle detected...')




# -------------------------- Testing ------------------------------
if __name__ == '__main__':
    # Create Nodes
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')
    node5 = Node('E')
    node6 = Node('F')
    node7 = Node('G')
    node8 = Node('H')

    # Create Edges
    # Edge Weight, Starting Vertex, Ending Vertex
    edge1 = Edge(5,node1, node2)
    edge2 = Edge(8, node1, node8)
    edge3 = Edge(9, node1, node5)
    edge4 = Edge(15, node2, node4)
    edge5 = Edge(12, node2, node3)
    edge6 = Edge(4, node2, node8)
    edge7 = Edge(7, node8, node3)
    edge8 = Edge(6, node8, node6)
    edge9 = Edge(5, node5, node8)
    edge10 = Edge(4, node5, node6)
    edge11 = Edge(20, node5, node7)
    edge12 = Edge(1, node6, node3)
    edge13 = Edge(13, node6, node7)
    edge14 = Edge(3, node3, node4)
    edge15 = Edge(11, node3, node7)
    edge16 = Edge(9, node4, node7)

    # Adjacency List, append edges
    node1.adjacencyList.append(edge1)
    node1.adjacencyList.append(edge2)
    node1.adjacencyList.append(edge3)
    node2.adjacencyList.append(edge4)
    node2.adjacencyList.append(edge5)
    node2.adjacencyList.append(edge6)
    node8.adjacencyList.append(edge7)
    node8.adjacencyList.append(edge8)
    node5.adjacencyList.append(edge9)
    node5.adjacencyList.append(edge10)
    node5.adjacencyList.append(edge11)
    node6.adjacencyList.append(edge12)
    node6.adjacencyList.append(edge13)
    node3.adjacencyList.append(edge14)
    node3.adjacencyList.append(edge15)
    node4.adjacencyList.append(edge16)

    # Vertex List
    vertexList = (node1, node2, node3, node4, node5, node6, node7, node8)
    edgeList = (edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge9, edge10, edge11, edge12, edge13, edge14, edge15, edge16)

    algorithm = BellmanFord()
    # Calculate Shortest Path with start Vertex node1 : "A"
    algorithm.calculateShortestPath(vertexList, edgeList, node1)
    # Get the Shortest Path from node1: "A" to node7: "G"
    algorithm.getShortestPath(node7)
    # Get the Shortest Path from node1: "A" to node4: "D"
    algorithm.getShortestPath(node4)

# ----------------------------- EOC -------------------------------