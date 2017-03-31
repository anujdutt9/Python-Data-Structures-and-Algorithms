# Ternary Search Tree Implementation in Python.

# Node Structure for the Tree
class Node(object):
    def __init__(self, character):
        self.character = character                                  # Character on each node
        self.leftNode = None
        self.middleNode = None
        self.rightNode = None
        self.value = 0                                              # Value for the Key

# Ternary Search Tree Implementation
class TST(object):
    def __init__(self):
        # Initialize the Root Node
        self.rootNode = None

    # Put Function to Insert a Node
    # We are using "0" as the index of the input string.
    # This helps to track that at which character of string the value is stored.
    def put(self, key, value):
        self.rootNode = self.putItem(self.rootNode, key, value, 0)  # 0 -> index of given string key

    # Function to put the Item/Value in the Tree
    def putItem(self, node, key, value, index):
        c = key[index]                                              # Character with a given key using Index

        # Create a Node for each character
        if node == None:
            node = Node(c)

        # If input character is alphabetically smaller than the previous character
        # Go to left else right or middle.

        # If we go to left or right, it means we are still on same character and it is either smaller or greater than the
        # current character. Hence, index value remains the same.

        # In case if it goes to the middle, that means the characters are incrementing, hence the index value increments.
        if c < node.character:
            node.leftNode = self.putItem(node.leftNode, key, value, index)
        elif c > node.character:
            node.rightNode = self.putItem(node.rightNode, key, value, index)
        elif index < len(key)-1:
            node.middleNode = self.putItem(node.middleNode, key, value, index+1)
        else:
            # if index = len(key), it means we are at the last character of the key.
            # Last character of the Key holds the "Value".
            node.value = value
        return node

    # Function to get an item from TST with a given Key.
    def get(self, key):
        node = self.getItem(self.rootNode, key, 0)
        if node == None:
            return -1               # Key not present in Dictionary
        return node.value

    # Function to get an item from the TST using Key
    def getItem(self, node, key, index):
        # If the node does not exists, return None
        if node == None:
            return None
        # Take the string character by character and traverse the tree.
        c = key[index]
        if c < node.character:
            return self.getItem(node.leftNode, key, index)
        elif c > node.character:
            return self.getItem(node.rightNode, key, index)
        elif index < len(key) - 1:
            return self.getItem(node.middleNode, key, index+1)
        else:
            # We are standing at that node, return this node
            return node


# ----------------- Testing --------------------
if __name__ == '__main__':
    tst = TST()
    tst.put('apple',100)
    tst.put('orange',200)

    print(tst.get('apple'))

# -------------------------- EOC ---------------------------------