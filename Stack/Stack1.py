class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty list to represent the stack
    
    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0
    
    # Push an element onto the stack
    def push(self, data):
        self.stack.append(data)  # Append to the end of the list
        print(f"Pushed {data} onto the stack.")
    
    # Pop an element from the stack (remove the top element)
    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        popped_data = self.stack.pop()  # Remove the last element
        print(f"Popped {popped_data} from the stack.")
        return popped_data
    
    # Peek at the top element without removing it
    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.stack[-1]  # Return the last element (top of the stack)

# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(f"Top element is {stack.peek()}")  # Should print 30

stack.pop()  # Should remove 30
stack.pop()  # Should remove 20

print(f"Top element is {stack.peek()}")  # Should print 10

stack.pop()  # Should remove 10
stack.pop()  # Stack is empty now, should print "Stack is empty"
