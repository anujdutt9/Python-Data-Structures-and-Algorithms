# AVL Tree
# On every insertion check if tree is balanced or not using height
# If it is unbalanced, make rotation to balance it


class Node(object):

    def __init__(self,data):
        self.data = data
        self.leftChild = None                               # Left Child to current node
        self.rightChild = None                              # Right cchild to current node
        self.height = 0                                     # Height of Tree to make sure tree is balanced


# Perform operations on AVL Tree
class AVL(object):
    def __init__(self):
        self.root = None                                    # Root Node

# --------------------------- Calculate Height of AVL Tree ---------------------------------
    def calcHeight(self,node):
        if not node:                                        # If this Node is Null
            return -1                                       # return -1; left and right child of leaf Nodes
        #print('\nHeight: ', node.height)
        return node.height

# ------------------------------- Insertion of Node in a AVL Tree ----------------------------
    def insert(self, data):
        self.root = self.insertNode(data, self.root)

    def insertNode(self, data, node):
        if not node:                                        # If it is a root node, create a new node
            return Node(data)
        if data < node.data:                                # If data < current node, go to left else right
            node.leftChild = self.insertNode(data, node.leftChild)
        else:
            node.rightChild = self.insertNode(data, node.rightChild)
        # Get the height of the new node
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        # Node has been inserted.
        # Now check if there has been any violations of AVL Tree
        #print('Node {} Inserted'.format(data))
        return self.settleViolation(data, node)


# -------------------- Settle any Violations upon adding/inserting new Node --------------------------
    def settleViolation(self, data, node):
        balance = self.calcBalance(node)
        # Case 1: Left Left Heavy situation
        if balance > 1 and data < node.leftChild.data:
            print("Left Left Heavy Situation...")
            return self.rotateRight(node)
        # Case 2: Right Right Heavy Situation
        if balance < -1 and data > node.rightChild.data:
            print('Right Right Heavy Situation...')
            return self.rotateLeft(node)
        # Case 3: Left Right Heavy Situation
        if balance > 1 and data > node.leftChild.data:
            print('Left Right Heavy Situation...')
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)
        # Case 4
        if balance < -1 and data < node.rightChild.data:
            print('Right Left Heavy Situation...')
            node.rightChild = self.rotateRight(node.rightChild)     # Here node is the Root Node
            return self.rotateLeft(node)
        return node


# ------------------------------- See if Tree is Balanced or not -------------------------------
    # If it returns value > 1, it means it is a Left heavy tree
    # Make Right rotation to balance it
    # If it returns value < 1, it means it is a Right heavy tree
    # Make Left rotation to balance it
    def calcBalance(self,node):
        if not node:
            return 0
        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)

    # Rotate Nodes to Right to Balance AVL Tree
    # O(1) time Complexity
    def rotateRight(self,node):
        print('Rotating to right on node ', node.data)      # C <- B <- D -> E; Root node is "D"
        tempLeftChild = node.leftChild                      # tempLeftChild => B
        t = tempLeftChild.rightChild                        # t = C

        # Rotate Right
        tempLeftChild.rightChild = node                     # "D" becomes right child of "B"; B -> D
        node.leftChild = t                                  # "C" becomes left child of "D"

        # Calculate Height of AVL Tree
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) + 1
        return tempLeftChild                                # Root Node after Rotation


    # Rotate Nodes to Left to Balance AVL Tree
    # O(1) time Complexity
    def rotateLeft(self,node):
        print('Rotating to Left on node ', node.data)
        tempRightChild = node.rightChild
        t = tempRightChild.leftChild

        # Rotate Right
        tempRightChild.leftChild = node
        node.rightChild = t

        # Calculate Height of AVL Tree
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightChild)) + 1
        return tempRightChild                                # Root Node after Rotation


# ------------------------------ Remove Node from AVL Tree -----------------------
    # Remove Node [Deletion]
    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):
        if not node:
            return node
        if data < node.data:
            node.leftChild = self.removeNode(data,node.leftChild)
        if data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:
                print('Removing a leaf node...')
                del node
                return None
            if not node.leftChild:
                print('Removing right child...')
                tempNode = node.rightChild
                del node
                return tempNode
            if not node.rightChild:
                print('Removing left child...')
                tempNode = node.leftChild
                return tempNode
            print('Removing Node with two children...')
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)
        if not node:
            return node

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        balance = self.calcBalance(node)

        # Doubly Left Heavy Tree
        if balance > 1 and self.calcBalance(node.leftChild) >= 0:
            return self.rotateRight(node)
        # Doubly Right Heavy Tree
        if balance < -1 and self.calcBalance(node.rightChild) <= 0:
            return self.rotateLeft(node)
        # Left Right Case
        if balance > 1 and self.calcBalance(node.leftChild) < 0:
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)
        # Right Left Case
        if balance < -1 and self.calcBalance(node.rightChild) > 0:
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node)
        return node


    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)
        return node


# --------------------- Traverse the AVL Tree ------------------
    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)


    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)
        print('%s' % node.data)
        if node.rightChild:
            self.traverseInOrder(node.rightChild)

# ------------------- Testing -----------------
if __name__ == '__main__':

    avl = AVL()
    avl.insert(10)
    avl.insert(20)
    avl.insert(5)
    avl.insert(6)
    avl.insert(15)
    avl.traverse()

    avl.remove(20)
    avl.remove(15)
    avl.traverse()

#---------------------------------------- EOC ------------------------------------