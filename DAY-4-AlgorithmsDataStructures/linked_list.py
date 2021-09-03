class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __str__(self):
        return f'{self.value}'


class LinkedList:
    def __init__(self, head_node=None):
        self.head_node = head_node

    def print_list(self):
        value_to_print = self.head_node
        while value_to_print is not None:
            print(value_to_print)
            value_to_print = value_to_print.next_node

    def add_at_the_begin(self, new_node):
        if not isinstance(new_node, Node):
            raise TypeError(f'{new_node} must be a Node type')
        new_node.next_node = self.head_node
        self.head_node = new_node

    def add_at_the_end(self, new_node):
        if not isinstance(new_node, Node):
            raise TypeError(f'{new_node} must be a Node type')

        last_node = self.head_node
        while last_node.next_node:
            last_node = last_node.next_node
        last_node.next_node = new_node

    def add_after_node(self, new_node, middle_node):
        if not isinstance(new_node, Node):
            raise TypeError(f'{new_node} must be a Node type')

        new_node.next_node = middle_node.next_node
        middle_node.next_node = new_node


c = Node('c')
a = Node('a')
b = Node(5)
c.next_node = a
a.next_node = b
link_list = LinkedList(c)
link_list.print_list()
print('*' * 50)

d = Node('d')
link_list.add_at_the_begin(d)
link_list.print_list()
print('*' * 50)

f = Node('f')
link_list.add_at_the_end(f)
link_list.print_list()
print('*' * 50)

e = Node('e')
link_list.add_after_node(e, a)
link_list.print_list()
print('*' * 50)
