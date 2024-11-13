def reverse_string(input_string):
    # Step 1: Initialize an empty stack
    stack = []

    # Step 2: Push each character of the string onto the stack
    for char in input_string:
        stack.append(char)

    # Step 3: Initialize an empty string to store the reversed string
    reversed_string = ""

    # Step 4: Pop characters from the stack and append them to the reversed string
    while stack:
        reversed_string += stack.pop()

    return reversed_string

# Example usage:
input_string = "Hello"
reversed_str = reverse_string(input_string)
print("Reversed String:", reversed_str)
