def Reverse(name, i, j):
    # base case
    if i > j:
        return
    
    # Swap the characters at position i and j
    name[i], name[j] = name[j], name[i]
    
    # Recursive call for the rest of the string
    Reverse(name, i + 1, j - 1)

# Convert string to list of characters
name = list("Rushikesh")

# Call the function
Reverse(name, 0, len(name) - 1)

# Convert list back to string
reversed_name = ''.join(name)

# Print the reversed string
print(reversed_name)
