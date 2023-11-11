class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1

    def append(self, value):
        new_node = Node(value)  # creating a new node
        # code first the corner case (if LL is emtpy, this means self.head = new_node, self.tail = new_node)
        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght += 1  # we increase the lenght of LL
        return True

    def pop(self):
        # 2 edge cases -> if LL is emtpy or if LL have only 1 item
        # two variables temp and pre, we check while temp is not None, and we move pre with temp - 1
        if self.lenght == 0:
            return None
        else:
            temp = self.head
            pre = self.head
            while temp.next:
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.lenght -= 1
            if self.lenght == 0:
                self.head = None
                self.tail = None
            # for testing, returning only the value
            # return temp.value
            return temp

    def pop_first(self):
        if self.lenght == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.lenght -= 1
        if self.lenght == 0:
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.lenght += 1
        return True

    def get(self, index):
        if index < 0 or index >= self.lenght:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.lenght:
            return False
        if index == 0:
            return self.prepend(value)
        elif index == self.lenght:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.lenght += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.lenght:
            return None
        if index == 0:
            return self.pop_first()
        elif index == self.lenght - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next  # this is O(1), and self.get() is O(n)
        prev.next = temp.next
        temp.next = None
        self.lenght -= 1
        return temp

    def reverse(self):  # watch the animation for some time
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.lenght):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    # Method to print all nodes inside LL
    def print_LL(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


if __name__ == "__main__":
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.print_LL()
    my_linked_list.reverse()
    # my_linked_list.insert(1, 1)
    # my_linked_list.append(23)
    # my_linked_list.append(7)
    # my_linked_list.append(3)
    # my_linked_list.prepend(1)
    # my_linked_list.print_LL()
    # print(my_linked_list.pop())
    # print(my_linked_list.pop())
    # print(my_linked_list.pop())
    # my_linked_list.pop_first()
    # my_linked_list.print_LL()
    # print(my_linked_list.get(2))
    # my_linked_list.print_LL()
    # my_linked_list.set_value(1, 4)
    # my_linked_list.remove(2)
    my_linked_list.print_LL()
