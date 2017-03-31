# Binary Search Tree

# Constructor to create a Node with Data and Left and Right Child
class Node(object):                                     # Nodes in Tree
    # Constructor
    def __init__(self, data):
        self.data = data                                # Input Data
        self.leftChild = None                           # Left Child
        self.rightChild = None                          # Right Child


# Operations on Binary Search Tree
class BinarySearchTree(object):
    # Constructor
    def __init__(self):
        self.root = None                                # Initialize Root as Null

# ------------------------- Insert a New Node in a Binary Search Tree ----------------------------
    # Insert an item to BST
    def insert(self,data):
        if not self.root:                               # If Root Node is empty, it is first element
            self.root = Node(data)                      # Create a new Node of Tree
        else:
            self.insertNode(data, self.root)            # If root node exists, insert a new node


    # Insert a New Node
    # O(log N) time Complexity if the Tree is Balanced
    def insertNode(self, data, node):
        # If New data is Less than the Root Node data
        if data < node.data:                            # If new item is less than current node data
            if node.leftChild:                          # If the current node[A] has a left child [B], then
                self.insertNode(data, node.leftChild)   # Insert a new node to left of [B]
            else:
                node.leftChild = Node(data)             # If there is no left child to [A], make a new Node to left of it.

        # If new data is Greater than the Root Node data
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)


# -------------------------- Remove Node from Binary Search Tree ---------------------------
    # Remove Node [Deletion]
    def remove(self,data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):
        if not node:                                    # If node is Empty i.e None, return the node
            return node

        # If data < root, traverse through the left child till we get the "data" node
        # Look for node we want to get rid of
        if data < node.data:                            # If the node data to be deleted is less than root, go to left
            node.leftChild = self.removeNode(data, node.leftChild) # Tell parent node that its left child is None
        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)

        # Else we are standing at that node which we want to delete.
        # It may be a node with children (1 or 2) or a leaf node
        else:
            # If the current node is a leaf node i.e no left and right child
            if not node.leftChild and not node.rightChild:
                print('Removing leaf node...')
                del node
                return None                             # Returning None tells its parent Node that its left or right child has been deleted
            # If the node to be deleted is a parent and has only one child (on right)
            # Node -> Right Child
            if not node.leftChild:
                print('Removing Node with single right child...')
                tempNode = node.rightChild              # Put the right child value in a temporary variable
                del node                                # Delete the parent node
                return tempNode                         # Return the temp node. Parent of deleted node --> Temp node

            # If the node to be deleted is a parent and has only one child (on Left)
            # Node -> Left Child
            elif not node.rightChild:
                print('Removing Node with single left child...')
                tempNode = node.leftChild
                del node
                return tempNode

            # If node to be deleted is a parent node with two children
            print('Removing node with two children...')
            # Fetch the largest node in left subtree to root in temp Node.
            tempNode = self.getPredecessor(node.leftChild)
            # Replace the node to be deleted data with the largest node value data
            node.data = tempNode.data
            # Remove the node with largest value in the left subtree to root/node to be deleted.
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)
        return node


    # Get the largest value in the left subtree of the root node
    # Return the node with largest value
    def getPredecessor(self,node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node


# -------------------------- Get the Minimum Value in a BST ---------------------------------
    # Get the Minimum Value in a BST
    # The left most value is the Smallest Value
    def getMinValue(self):
        if self.root:                                   # If Tree not empty
            return self.getMin(self.root)               # Go to getMin function


    # Traverse to the left most node (smallest value)
    def getMin(self,node):                              # Start traversing from root node
        if node.leftChild:                              # If left child exists keep going till we hit "NONE"
            return self.getMin(node.leftChild)
        return node.data                                # When we hit None, we get the left most node and return its data


# ---------------------------- Get the Maximum Value in a BST ----------------------------------
    # Get Maximum Value from BST (Right most value)
    def getMaxValue(self):
        if self.root:                                   # If at root node, go to get Max function
            return self.getMax(self.root)

    # Traverse to the right most value (max value)
    def getMax(self, node):
        if node.rightChild:                             # If right child exists, traverse to right most node
            return self.getMax(node.rightChild)
        return node.data                                # Return the right most node data


# ------------------------------ Binary Search Tree Traversal --------------------------------------
    # Traverse through a BST
    def traversal(self):
        if self.root:                                   # If at root node, go to traverseInOrder function
            self.traverseInOrder(self.root)

    # Traversing BST In Order: Left -> Root -> Right
    def traverseInOrder(self,node):
        if node.leftChild:                              # If left child to root node exists, go on to left most node
            self.traverseInOrder(node.leftChild)
        print('%s' % node.data)                         # Print the root node
        if node.rightChild:                             # If right child to root node exists, go on to nodes on right
            self.traverseInOrder(node.rightChild)


    # Traversing BST Pre Order: Root -> Left -> Right
    def traversePreOrder(self, node):
        print('%s' % node.data)                         # Print the root node
        if node.leftChild:                              # If left child to root node exists, go on to left most node
            self.traversePreOrder(node.leftChild)
        if node.rightChild:                             # If right child to root node exists, go on to nodes on right
            self.traversePreOrder(node.rightChild)

    # Traversing BST Pre Order: Left -> Right -> Root
    def traversePostOrder(self, node):
        if node.leftChild:                              # If left child to root node exists, go on to left most node
            self.traversePostOrder(node.leftChild)
        if node.rightChild:                             # If right child to root node exists, go on to nodes on right
            self.traversePostOrder(node.rightChild)
        print('%s' % node.data)                         # Print the root node



# -------------------- Testing -----------------------
if __name__ == '__main__':

    bst = BinarySearchTree()
    bst.insert(10)                  # ROOT Node
    bst.insert(13)
    bst.insert(14)
    bst.insert(5)
    bst.insert(1)

    #bst.remove(5)
    bst.remove(10)

    # bst.insert('A')
    # bst.insert('C')
    # bst.insert('G')
    # bst.insert('Z')

    bst.traversal()

# --------------------- EOC ----------------------