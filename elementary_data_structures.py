# Part 2: Elementary Data Structures Implementation and Discussion

# 1. Arrays and Matrices
class Array:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size

    def insert(self, index, value):
        """Insert an element at the specified index."""
        if index >= 0 and index < self.size:
            self.array[index] = value
        else:
            print("Index out of bounds.")

    def delete(self, index):
        """Delete an element at the specified index."""
        if index >= 0 and index < self.size:
            self.array[index] = None
        else:
            print("Index out of bounds.")

    def access(self, index):
        """Access an element at the specified index."""
        if index >= 0 and index < self.size:
            return self.array[index]
        else:
            return "Index out of bounds."

    def display(self):
        """Display the array."""
        return self.array


# 2. Stacks using Arrays
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        """Push an element onto the stack."""
        self.stack.append(value)

    def pop(self):
        """Pop an element from the stack."""
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        """Peek at the top element of the stack."""
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0


# 3. Queues using Arrays
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        """Enqueue an element to the queue."""
        self.queue.append(value)

    def dequeue(self):
        """Dequeue an element from the queue."""
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        """Peek at the front element of the queue."""
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0


# 4. Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        """Insert a node at the end of the linked list."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete(self, value):
        """Delete the first node with the specified value."""
        temp = self.head
        if temp is None:
            print("List is empty.")
            return
        if temp.data == value:
            self.head = temp.next
            return
        while temp:
            if temp.next and temp.next.data == value:
                temp.next = temp.next.next
                return
            temp = temp.next
        print(f"Value {value} not found.")

    def display(self):
        """Display the linked list."""
        temp = self.head
        elements = []
        while temp:
            elements.append(temp.data)
            temp = temp.next
        return elements


# Example Usage:
# Arrays
arr = Array(5)
arr.insert(0, 10)
arr.insert(1, 20)
arr.insert(2, 30)
print("Array:", arr.display())
arr.delete(1)
print("Array after deletion:", arr.display())

# Stack
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print("Stack top:", stack.peek())
print("Popped element:", stack.pop())
print("Stack after pop:", stack.stack)

# Queue
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("Queue front:", queue.peek())
print("Dequeued element:", queue.dequeue())
print("Queue after dequeue:", queue.queue)

# Linked List
linked_list = LinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)
print("Linked List:", linked_list.display())
linked_list.delete(20)
print("Linked List after deletion:", linked_list.display())
