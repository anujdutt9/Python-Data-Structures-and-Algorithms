# Queues using Arrays (Lists)

class Queue(object):

    def __init__(self):
        self.queue = []                     # Create an empty list

    def isEmpty(self):
        return self.queue == []             # If Queue is empty return True else False


    def enqueue(self,data):
        self.queue.insert(0,data)           # Add data to Queue at 0th Index. i.e. starting of list[0 1 2 3 ...]
        return '{} added to Queue'.format(data)


    def dequeue(self):
        return self.queue.pop()             # Pop the item from Queue (list); pops out the last item which is 1st in Queue


    def queueSize(self):
        return 'Size of Queue: {}'.format(len(self.queue))   # Queue size = length of list


# Testing
if __name__ == '__main__':
    queue = Queue()
    print(queue.enqueue('Anuj'))
    print(queue.enqueue(9))
    print(queue.enqueue(20))

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.queueSize())
    print(queue.dequeue())
    print(queue.queueSize())

# --------------------- EOC -----------------