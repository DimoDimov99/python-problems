class ListStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def print_ls(self):
        print(self.items)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LLStack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1


if __name__ == "__main__":
    # ls = ListStack()
    # ls.add_item(1)
    # ls.add_item(2)
    # ls.add_item(3)
    # ls.add_item(4)
    # print(ls.peek())
    # ls.remove_item()
    # ls.print_ls()
    # ls2 = ListStack()
    # ls2.add_item(5)
    # ls2.print_ls()
    lls = LLStack(4)
    lls.print_stack()
    lls.push(5)
    lls.print_stack()
