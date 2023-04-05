# This class contains implementation of an array stack.
class Stack():

    # Declares an initially empty stack
    def __init__(self):
        self.size = 0
        self.stack = []

    # Pushes an item to the top of the stack
    def push(self, item):
        self.stack.append(item)
        self.size += 1

    # Removes the top item from the stack
    def pop(self):
        if (self.size <= 0):
            print("You are attempting to delete from an empty stack.")
            print("In a proper code environment we would throw an exception here")
        else:
            self.size -= 1
            return self.stack.pop()

    # Returns the top item of the stack (without removing it)
    def peek(self):
        if (self.size == 0):
            print("Currently the stack is empty!")
        else:
            return self.stack[self.size - 1]

    # Returns the size of the stack
    def get_size(self):
        return self.size

    # Tostring method for the stack
    def __str__(self):
        result = ""
        for i in range(len(self.stack) - 1, -1, -1):
            result += "Item %d: %s\n" % ((i), self.stack[i])

        return result


class StackQueue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.size = 0

    def enqueue(self, data):
        self.stack1.push(data)

    def dequeue(self):
        if self.stack2.get_size() == 0:
            while self.stack1.get_size() > 0:
                self.stack2.push(self.stack1.pop())

        if self.stack2.get_size() == 0:
            return None

        self.size -= 1
        return self.stack2.pop()

    def __str__(self):
        return "The contents of the StackQueue are:\n\nStack1:\n%s\n\nStack2:\n%s" % (self.stack1, self.stack2)


def main():
    print("We will design an implementation of a queue that instead of a linked list or array holding the data, we will have two stacks to hold the data.")

    my_queue = StackQueue()
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.enqueue(4)
    my_queue.enqueue(5)
    print(my_queue)
    my_queue.dequeue()
    my_queue.dequeue()
    print(my_queue)
    my_queue.enqueue(6)
    print(my_queue)
    my_queue.enqueue(7)
    my_queue.dequeue()
    print(my_queue)


main()
