# Linked Lists
# We are only given the head of the linked list.

# Make a Linked List Node Class
class Node(object):
    # Constructor
    def __init__(self,data):
        self.data = data                        # Data to be stored
        self.nextNode = None                    # Pointer to next Node; Initialized to "None"

# Linked List head (root node) and size
class LinkedList(object):
    def __init__(self):
        self.head = None                        # head -> first node in Linked List; initially "None"
        self.size = 0                           # Initial size of Linked List


# ------------------ Insertion at Starting of Linked List -----------------
    # Insert a New Node to starting of Linked List
    # O(1) time Complexity
    def insertStart(self,data):
        self.size += 1                          # Increment the size of Linked List by 1
        newNode = Node(data)                    # Create a new Node with input "data"
        if not self.head:                       # If head = NULL i.e it is first node in Linked List
            self.head = newNode                 # new value "data" assigned to new Node
        else:                                   # If head != Null i.e this is not the first node
            newNode.nextNode = self.head        # Point the Pointer of "New Node" to current "Head Node"
            self.head = newNode                 # and make the "New Node" the "Head Node"
        return 'Node {} added to Head of Linked List'.format(data)

# --------------- Size of Linked List ------------------
    # Size of Linked List
    # O(1) time Complexity as we are currently at root and adding a new node here
    def linkedListSize(self):
        return self.size                        # Returns the size of linked list

    # Size of Linked List by traversing through Linked List
    #  O(N) time Complexity
    def linkedListSize2(self):
        actualNode = self.head                  # Go to the first node in linked list
        size = 0                                # Intialize size variable
        while actualNode is not None:           # Traverse and Count till we do not reach the last node i.e Pointer = Null
            size += 1                           # Increment size
            actualNode = actualNode.nextNode    # Go to next node
        return size                             # Return total size

# ----------------- Insertion at End of Linked List --------------------------
    # Insertion at the end of Linked List
    # O(N) time Complexity as you need to traverse through whole list
    def insertEnd(self,data):
        self.size += 1                          # Increment size of Linked List
        newNode = Node(data)                    # Create a new node
        actualNode = self.head                  # Point the variable to head of Linked List

        while actualNode.nextNode is not None:  # Traverse through the linked list till the Pointer = NULL
            actualNode = actualNode.nextNode
        actualNode.nextNode = newNode           # If Pointer = Null, take the current "Node" and point to "New Node"
        return 'Node {} added to End of Linked List'.format(data)

# ------------------- Node Removal from Linked List ------------------
    def removeNode(self,data):
        if self.head is None:                   # If Linked List is empty
            return
        self.size -= 1
        currentNode = self.head                 # Initialize current node as root
        previousNode = None                     # Initialize no previous Node at begenning

        while currentNode.data != data:         # Traverse through the Linked List for the "data"
            previousNode = currentNode          # Currently traversed node becomes previous node and move to next node
            currentNode = currentNode.nextNode  # "Next node" to "current node" becomes the "new current node"

        if previousNode is None:                # If the "data" Node to be deleted is the "First Node"
            self.head = currentNode.nextNode    # Make the "Next Node" to current Node the Head
        else:
            previousNode.nextNode = currentNode.nextNode    # Make previous node to current data Node to point to Node next to data Node
        return 'Node {} Removed from Linked List'.format(data)


# ------------ Traverse the List ---------------
    # Linked List Traversal
    # Print out the elements of Linked List
    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print('%d' % actualNode.data)
            actualNode = actualNode.nextNode

# ------------ Testing the Linked List Data Structure -----------------
if __name__ == '__main__':

	linked_List = LinkedList()
	print(linked_List.insertStart(12))                     # Insert 12 at starting of Linked List
	print(linked_List.insertStart(122))                    # Insert 122;  LL: 122 -> 12
	print(linked_List.insertStart(3))                      # Insert 3;    LL: 3 -> 122 -> 12
	print(linked_List.insertEnd(31))                       # Insert 31;   LL: 3 -> 122 -> 12 -> 31
	linked_List.traverseList()
	print('Size of Linked List: ',linked_List.linkedListSize())
	print(linked_List.removeNode(31))
	print('Size of new Linked List: ',linked_List.linkedListSize())
	print(linked_List.removeNode(122))
	print('Size of new Linked List: ',linked_List.linkedListSize())
	print(linked_List.removeNode(3))
	print('Size of new Linked List: ',linked_List.linkedListSize())
	print(linked_List.removeNode(12))
	print('Size of new Linked List: ',linked_List.linkedListSize())

# -------------------------- EOC --------------------------