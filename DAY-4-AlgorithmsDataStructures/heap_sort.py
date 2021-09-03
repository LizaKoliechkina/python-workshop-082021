class Heap:
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if self.value is None:
            self.value = value
        else:
            if value < self.value:
                if self.left is None:
                    self.left = Heap(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Heap(value)
                else:
                    self.right.insert(value)

    def print_heap(self):
        if self.left:
            self.left.print_heap()
        print(self.value)
        if self.right:
            self.right.print_heap()


list_to_sort = [1, 18, 5, 223, 49, 19, 8]
h = Heap()

for n in list_to_sort:
    h.insert(n)

h.print_heap()
