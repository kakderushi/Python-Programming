def isPalindrome(name, i, j):
    # base case: if indices cross, it means we've checked the whole string
    if i >= j:
        return True
    
    # if characters at i and j are not equal, it's not a palindrome
    if name[i] != name[j]:
        return False
    
    # recursive call to check the remaining part of the string
    return isPalindrome(name, i + 1, j - 1)

# Test with a string
name = "madam"

# Call the function
result = isPalindrome(name, 0, len(name) - 1)

# Print the result
if result:
    print(f"'{name}' is a palindrome.")
else:
    print(f"'{name}' is not a palindrome.")
