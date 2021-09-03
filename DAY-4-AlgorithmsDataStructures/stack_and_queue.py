class Stack:
    def __init__(self, stack=None):
        self.stack = stack if stack else []

    def __str__(self):
        return f'{self.stack}'

    def add(self, value):
        self.stack.append(value)

    def remove(self):
        if len(self.stack) <= 0:
            return 'Empty stack'
        return self.stack.pop()


stack = Stack()
stack_1 = Stack([1, 2, 3])
print(stack_1)
stack.add('string')
stack.add(52)
print(stack.remove())
print(stack.remove())
print(stack.remove())
print(stack.remove())
print(stack.remove())
print(stack.remove())


class Queue:
    def __init__(self, queue=None):
        self.queue = queue if queue else []

    def __str__(self):
        return f'{self.queue}'

    def add(self, value):
        self.queue.insert(0, value)

    def remove(self):
        if len(self.queue) <= 0:
            return 'Empty queue'
        return self.queue.pop()


q = Queue()
q1 = Queue([1, 2, 3])
print(q1)
q.add('string')
q.add(52)
print(q.remove())
print(q.remove())
print(q.remove())
print(q.remove())
print(q.remove())
print(q.remove())
