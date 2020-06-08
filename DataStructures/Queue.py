from Node import Node

class Queue(object):

    def __init__(self, head: Node = None):
        self.head: Node = head
        self.tail: Node = head

    def enqueue(self, node: Node):
        """
        Enqueue a given node
        :param node: Node to be enqueue
        :return: void
        """
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def enqueue(self, value):
        """
        Enqueue a Node that contains the given value
        :param value: Value to be enqueue
        :return: void
        """
        node = Node(value=value)
        self.enqueue(node)

    def dequeue(self) -> Node:
        """
        Dequeue the head of the queue
        :return: Head of the Queue
        """
        if self.head is None:
            return None
        else:
            response = self.head
            self.head = self.head.next
            return response

    def __iter__(self):
        '''
        Implementation of iterator protocol, using yield keyword to dynamically return the next
        value of the queue without the need to store everything
        :return:
        '''
        actual = self.head
        while actual is not None:
            yield actual
            actual = actual.next

    __doc__ = 'Is a class representation of a Node based Queue, where the class contains the first and last node of the Queue for efficientcy, ' \
              'and every node knows its next node. The value stored in the nodes can be of any type. For certain applications is better for that ' \
              'value to be one single type throughout all the nodes of the queue'
