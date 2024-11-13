def solve(inputStack, N, cnt):
    # Base case: when we've reached the middle element
    if cnt == N // 2:
        inputStack.pop()
        return
    
    # Pop the top element and store it
    num = inputStack.pop()

    # Recursive call to move closer to the middle
    solve(inputStack, N, cnt + 1)
    
    # After the middle element is deleted, push the stored elements back
    inputStack.append(num)

def deleteMiddle(inputStack, N):
    cnt = 0
    solve(inputStack, N, cnt)

# Example usage:
inputStack = [1, 2, 3, 4, 5]
N = len(inputStack)
deleteMiddle(inputStack, N)
print(inputStack)
