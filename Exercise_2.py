
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None
 
class Stack:
    def __init__(self):
        self.stack = Node(None)
        
    def push(self, data):
        if self.stack.data is None:
            self.stack.data = data
        else:
            new_node = Node(data)
            new_node.next = self.stack
            self.stack = new_node

    def pop(self):
        if self.stack.data is None:
            return None
        data = self.stack.data
        self.stack = self.stack.next
        return data

    def isEmpty(self):
        return self.stack.data is None

    def peek(self):
        return self.pop()

    def size(self):
        if self.isEmpty():
            return 0
        length = 0
        temp = self.stack
        while temp is not None:
            length += 1
            temp = temp.next
        return length

    def show(self):
        stack = []
        temp = self.stack
        while temp is not None:
            stack.append(temp.data)
            temp = temp.next
        return stack    

a_stack = Stack()
while True:
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    print('push <value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
    #Give input as string if getting an EOF error. Give input like "push 10" or "pop"
    operation = do[0].strip().lower()
    if operation == 'push':
        a_stack.push(int(do[1]))
    elif operation == 'pop':
        popped = a_stack.pop()
        if popped is None:
            print('Stack is empty.')
        else:
            print('Popped value: ', int(popped))
    elif operation == 'quit':
        break
    elif operation == 'show':
        print(a_stack.show())
