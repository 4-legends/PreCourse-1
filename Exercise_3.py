class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        print("Current Data: ", self.data)
        print("Next Data: ", self.next.data)
        return ""
    
class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = ListNode()

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if self.head.data is None:
            self.head.data = data
        else:
            new_node = ListNode(data)
            new_node.next = self.head
            self.head = new_node
        
    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        temp = self.head
        while temp is not None:
            if temp.data == key:
                return temp
            temp = temp.next
        return None
        
    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        temp = self.head
        prev = None
        while temp is not None:
            if temp.data == key:
                if prev is not None:
                    prev.next = temp.next
                else:
                    self.head = temp.next
                return
            prev = temp
            temp = temp.next
        return None

    def show(self):
        """
        Shows the elements of the list
        """
        stack = []
        temp = self.head
        while temp is not None:
            stack.append(temp.data)
            temp = temp.next
        return stack
    
a = SinglyLinkedList()
a.append(1)
a.append(2)
a.append(3)
print(a.show())
a.remove(2)
a.append(4)
print(a.show())
print(a.find(3))