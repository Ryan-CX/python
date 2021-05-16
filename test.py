class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
   
    def __init__(self):
        self._head = None

    def add(self, val):
        """
        Adds a node containing val to the linked list
        """
        if self._head is None:  # If the list is empty
            self._head = Node(val)
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = Node(val)

    def display(self):
        """
        Prints out the values in the linked list
        """
        current = self._head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def remove(self, val):
        """
        Removes the node containing val from the linked list
        """
        if self._head is None:  # If the list is empty
            return

        if self._head.data == val:  # If the node to remove is the head
            self._head = self._head.next
        else:
            current = self._head
            while current is not None and current.data != val:  #1,2,3 => 2,3
                previous = current
                current = current.next
            if current is not None:  # If we found the value in the list
                previous.next = current.next

    def is_empty(self):
        """
        Returns True if the linked list is empty,
        returns False otherwise
        """
        return self._head is None
        
    def to_regular_list(self):
        """
        Returns a regular Python list containing the same values, in the same order, as the linked list
        """
        result = []
        current = self._head
        while current is not None:
            result += [current.data]
            current = current.next
        return result

    def reverse(self):
        current = self._head
        while current.next != None:    #1,2,3
            temp = current             #temp = 1,
            current = current.next      # 2,2,3
            current.next = temp         #  2,1



    def add_recursive(self,data):
        if self._head is None:  # If the list is empty
            self._head = Node(data)

        else:
            def helper(node):
                if not node:
                    return Node(data)
                else:
                    node.next = helper(node.next)
                return node
                
            self._head = helper(self._head)
        









list1 = LinkedList()
list1._head = Node('a')
e2 = Node('b')
e3 = Node('c')
list1._head.next = e2
e2.next = e3
list1.add_recursive('d')
list1.display()
