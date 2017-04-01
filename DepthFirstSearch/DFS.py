# Depth First Search

class Node(object):
    def __init__(self, name):
        # Name of the new node
        self.name = name
        # List of Neighbors to the node
        self.adjacencyList = []
        # Status of node if visited or not
        self.visited = False
        # Predecessor of the node if any
        # Used in Shortest Path Algorithm
        self.predecessor = None


# Depth First Search
class DepthFirstSearch(object):

    # Depth First Search using Recursion
    def dfs_Recursive(self, node):
        node.visited = True
        print('%s' % node.name)
        for n in node.adjacencyList:
            if not n.visited:
                self.dfs_Recursive(n)

    # Depth First Search using Iterative Method
    def dfs_Iterative(self, node):
        # Initialize Stack object
        stack = []
        # Push the current node to Stack
        stack.append(node)
        # Set current node visited to True
        node.visited = True
        # While the stack is not empty, go on
        while stack:
            # Pop the current node value
            actualNode = stack.pop()
            print('%s' % actualNode.name)
            # For Neighbors of Current Node
            for n in actualNode.adjacencyList:
                if not n.visited:
                    n.visited = True
                    stack.append(n)


# Testing
if __name__ == '__main__':
    # Depth First Search Recursively
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')
    node5 = Node('E')

    node1.adjacencyList.append(node2)
    node1.adjacencyList.append(node3)
    node2.adjacencyList.append(node4)
    node4.adjacencyList.append(node5)

    dfs = DepthFirstSearch()
    print('DFS Recursively:\n')
    dfs.dfs_Recursive(node1)


    # Depth First Search Iteratively
    node1 = Node('A')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')
    node5 = Node('E')

    node1.adjacencyList.append(node2)
    node1.adjacencyList.append(node3)
    node2.adjacencyList.append(node4)
    node4.adjacencyList.append(node5)

    print('\nDFS Iteratively:\n')
    dfs.dfs_Iterative(node1)

# ------------------------ EOC -------------------------